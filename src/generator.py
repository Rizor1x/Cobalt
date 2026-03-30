import textwrap
from lark import Transformer
from error import CrestError

class RustGen(Transformer):
    def __init__(self, code, file_path):
        self.code = code
        self.file_path = file_path
        self.level = 0
        super().__init__()

    # --- УТИЛИТЫ И ОШИБКИ ---
    def error(self, message, token, help_msg=""):
        raise CrestError(message, token, self.code, self.file_path, help_msg)

    # 1. ТОЧКА ВХОДА И БЛОКИ КОДА

    def start(self, statements):
        global_scope =[]
        main_scope =[]

        # Умное разделение: выносим функции и классы из main() в глобальную область
        for stmt in statements:
            if stmt.startswith("fn ") or stmt.startswith("#[derive"):
                global_scope.append(stmt)
            else:
                main_scope.append(stmt)

        globals_code = "\n\n".join(global_scope)
        main_code = "\n    ".join(main_scope)

        runtime_helpers = textwrap.dedent("""
        // --- Crest Runtime ---
        use std::io::Write;

        #[allow(dead_code)]
        fn __crest_input(prompt: &str) -> String {
            print!("{}", prompt);
            std::io::stdout().flush().unwrap();
            let mut buf = String::new();
            std::io::stdin().read_line(&mut buf).unwrap();
            buf.trim().to_string()
        }
        // ---------------------
        """).strip()

        return f"{runtime_helpers}\n\n{globals_code}\n\nfn main() {{\n    {main_code}\n}}"
    
    def block(self, items):
        self.level += 1
        indent = "    " * self.level
        code = f"\n{indent}".join(items)
        self.level -= 1
        return f"{{\n{indent}{code}\n{'    ' * self.level}}}"

    # 2. ООП (КЛАССЫ И МЕТОДЫ)

    def class_var(self, items):
        name = items[1].value
        t_token = items[2]
        return ("field", name, t_token)

    def class_stmt(self, items):
        class_name = items[0].value
        fields = []
        methods =[]

        valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}

        for item in items[1:]:
            if isinstance(item, tuple) and item[0] == "field":
                name = item[1]
                t_token = item[2]
                t_name = t_token.value
                if t_name not in valid_types:
                    self.error(f"Неизвестный тип поля '{t_name}'", t_token)
                fields.append(f"{name}: {valid_types[t_name]}")
            else:
                methods.append(item)

        fields_str = ",\n    ".join(fields)
        methods_str = "\n    ".join(methods)

        struct_def = f"#[derive(Debug, Clone)]\nstruct {class_name} {{\n    {fields_str}\n}}"
        impl_def = f"impl {class_name} {{\n    {methods_str}\n}}"

        return f"{struct_def}\n{impl_def}"

    def prop_access(self, items):
        obj_name = items[0].value
        prop_name = items[1].value
        return f"{obj_name}.{prop_name}"

    def method_call(self, items):
        obj_name = items[0].value
        method_name = items[1].value
        args = items[2] if len(items) > 2 and items[2] is not None else ""
        
        call = f"{obj_name}.{method_name}({args})"
        if method_name == "len":
            return f"({call} as i32)"
        return call

    def method_call_stmt(self, items):
        return f"{items[0]};"

    # 3. ФУНКЦИИ

    def fn_stmt(self, items):
        name = items[0].value
        args = items[1] if items[1] is not None else ""
        
        ret_type = ""
        if items[2] is not None:
            t_token = items[2]
            t_name = t_token.value
            valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}
            
            if t_name not in valid_types:
                self.error(f"Неизвестный тип возврата '{t_name}'", t_token, "Доступные типы: int, float, str, bool.")
            ret_type = f" -> {valid_types[t_name]}"
            
        block_code = items[3]
        return f"fn {name}({args}){ret_type} {block_code}"

    def return_stmt(self, items):
        return f"return {items[0]};"

    def param(self, items):
        if len(items) == 1:
            name = items[0].value
            return "&self" if name == "self" else name
            
        if len(items) == 2 and items[0].value == "var":
            name = items[1].value
            return "&mut self" if name == "self" else f"mut {name}"

        name = items[0].value
        t_token = items[1]
        t_name = t_token.value
        valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}
        
        if t_name not in valid_types:
            self.error(f"Неизвестный тип аргумента '{t_name}'", t_token)
            
        return f"{name}: {valid_types[t_name]}"

    def params(self, items):
        return ", ".join(items)

    def arguments(self, items):
        return ", ".join([str(i) for i in items])

    def fn_call(self, items):
        name = items[0].value
        args = items[1] if len(items) > 1 and items[1] is not None else ""
            
        if name == "input":
            prompt_arg = f"&{args}" if args else '""'
            return f"__crest_input({prompt_arg})"
            
        return f"{name}({args})"

    def fn_call_stmt(self, items):
        return f"{items[0]};"

    # 4. УПРАВЛЕНИЕ ПОТОКОМ (If, While, For)

    def if_stmt(self, items):
        cond = items[0]
        if_block = items[1]
        if len(items) == 3:
            return f"if {cond} {if_block} else {items[2]}"
        return f"if {cond} {if_block}"

    def while_stmt(self, items):
        return f"while {items[0]} {items[1]}"

    def for_stmt(self, items):
        iterator_name = items[0].value
        start_val = items[1]
        end_val = items[3]
        f_block = items[4]
        return f"for {iterator_name} in {start_val}..{end_val} {f_block}"


    # 5. ПЕРЕМЕННЫЕ И БАЗОВЫЕ КОМАНДЫ

    def decl_with_type(self, items):
        var_type = "let" if items[0].value == "val" else "let mut"
        var_name = items[1].value
        t_token = items[2]
        t_name = t_token.value 

        valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}
        if t_name not in valid_types:
            self.error(f"Неизвестный тип данных '{t_name}'", t_token)

        return f"{var_type} {var_name}: {valid_types[t_name]} = {items[3]};"
    
    def decl_no_type(self, items):
        var_type = "let" if items[0].value == "val" else "let mut"
        return f"{var_type} {items[1].value} = {items[2]};"
    
    def assign_stmt(self, items):
        return f"{items[0].value} = {items[1]};"
        
    def print_stmt(self, items):
        return f'println!("{{}}", {items[0]});'

    # 6. КОЛЛЕКЦИИ (Списки и Словари)

    def list_expr(self, items):
        if len(items) > 0 and items[0] is not None:
            return f"vec![{items[0]}]"
        return "vec![]"

    def dict_item(self, items):
        return f"({items[0]}, {items[1]})"

    def dict_items(self, items):
        return ", ".join(items)

    def dict_expr(self, items):
        if len(items) > 0 and items[0] is not None:
            return f"std::collections::HashMap::from([{items[0]}])"
        return "std::collections::HashMap::new()"

    def index_expr(self, items):
        name = items[0].value
        index_val = str(items[1])
        if ".to_string()" in index_val or '"' in index_val:
            return f"{name}[&({index_val})]"
        return f"{name}[({index_val}) as usize]"

    # 7. МАТЕМАТИКА И ЛОГИКА

    def condition(self, items):
        res =[]
        mapping = {"and": "&&", "or": "||", "==": "==", "!=": "!=", ">": ">", "<": "<", ">=": ">=", "<=": "<="}
        for i in items:
            val = getattr(i, 'value', str(i))
            res.append(mapping.get(val, val))
        return " ".join(res)

    def cmp_expr(self, items):
        return " ".join([str(getattr(i, 'value', i)) for i in items])

    def term(self, items):
        return " ".join([getattr(i, 'value', str(i)) for i in items])

    def factor(self, items):
        return " ".join([getattr(i, 'value', str(i)) for i in items])

    # 8. ПРИМИТИВЫ

    def number(self, items): return items[0].value
    def int_num(self, items): return items[0].value
    def float_num(self, items): return items[0].value
    def string(self, items): return f"{items[0].value}.to_string()"
    def var_name(self, items): return items[0].value