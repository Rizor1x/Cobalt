from lark import Transformer
from error import CrestError

class RustGen(Transformer):
    def __init__(self, code, file_path):
        self.code = code
        self.file_path = file_path
        self.level = 0
        super().__init__()

    def start(self, statements):
        code = "\n    ".join(statements)
        return f"fn main() {{\n    {code}\n}}"
    
    def block(self, items):
        self.level += 1
        indent = "    " * self.level

        code = f"\n{indent}".join(items)

        self.level -= 1
        return f"{{\n{indent}{code}\n{'    ' * self.level}}}"
    
    def condition(self, items):
        res = []
        for i in items:
            val = getattr(i, 'value', str(i))

            mapping = {
                "and": "&&",
                "or": "||",
                "==": "==", "!=": "!=", ">": ">", "<": "<", ">=": ">=", "<=": "<="
            }
            res.append(mapping.get(val, val))
            
        return " ".join(res)

    def return_stmt(self, items):
        # Возврат из функции
        expr = items[0]
        return f"return {expr};"

    def param(self, items):
        # Параметр функции, например: a: int
        name = items[0].value
        t_token = items[1]
        t_name = t_token.value
        
        valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}
        
        if t_name not in valid_types:
            raise CrestError(f"Неизвестный тип аргумента '{t_name}'", t_token, self.code, self.file_path)
            
        return f"{name}: {valid_types[t_name]}"

    def params(self, items):
        # Склеиваем параметры через запятую: a: i32, b: i32
        return ", ".join(items)

    def fn_stmt(self, items):
        name = items[0].value
        
        # 1. Обрабатываем аргументы (если они есть)
        args = ""
        if items[1] is not None:
            args = items[1] # Это уже склеенная строка из метода params
            
        # 2. Обрабатываем тип возврата (если он есть)
        ret_type = ""
        if items[2] is not None:
            t_token = items[2]
            t_name = t_token.value
            valid_types = {"int": "i32", "float": "f64", "str": "String", "bool": "bool"}
            
            if t_name not in valid_types:
                raise CrestError(
                    message=f"Неизвестный тип возврата '{t_name}'",
                    token=t_token,
                    code=self.code,
                    file_path=self.file_path,
                    help_msg="Доступные типы: int, float, str, bool."
                )
            ret_type = f" -> {valid_types[t_name]}"
            
        # 3. Блок кода
        block_code = items[3]
        
        return f"fn {name}({args}){ret_type} {block_code}"

    def while_stmt(self, items):
        cond = items[0]
        w_block = items[1]
        return f"while {cond} {w_block}"

    def for_stmt(self, items):
        iterator_name = items[0].value
        start_val = items[1]
        end_val = items[3]
        f_block = items[4]

        return f"for {iterator_name} in {start_val}..{end_val} {f_block}"

    def if_stmt(self, items):
        cond = items[0]
        if_block = items[1]
        
        if len(items) == 3:
            else_block = items[2]
            return f"if {cond} {if_block} else {else_block}"
        else:
            return f"if {cond} {if_block}"
    
    def arguments(self, items):
        # items - это список сгенерированных строк-выражений (например:["10", "5"])
        # Просто склеиваем их через запятую
        return ", ".join(items)

    def fn_call(self, items):
        # Вызов функции: name(args)
        name = items[0].value
        
        args = ""
        # Если аргументы есть, они будут в items[1]
        if len(items) > 1:
            args = items[1]
            
        return f"{name}({args})"

    def fn_call_stmt(self, items):
        # Если вызов функции - это отдельная строчка (как greet("Rizor1x")), 
        # нам нужно добавить точку с запятой в конце для Rust!
        call_str = items[0]
        return f"{call_str};"

    def decl_with_type(self, items):
        var_type = "let" if items[0].value == "val" else "let mut"
        var_name = items[1].value

        t_token = items[2]
        t_name = t_token.value 

        valid_types = {
            "int": "i32",
            "float": "f64",
            "str": "String",
            "bool": "bool"
        }

        if t_name not in valid_types:
            raise CrestError(
                message=f"Неизвестный тип данных '{t_name}'",
                token=t_token,
                code=self.code,
                file_path=self.file_path,
                help_msg="Доступные типы: int, float, str, bool."
            )

        type_name = valid_types[t_name]
        var_value = items[3]    

        return f"{var_type} {var_name}: {type_name} = {var_value};"
    
    def decl_no_type(self, items):
        var_type = "let" if items[0].value == "val" else "let mut"
        var_name = items[1].value
        var_value = items[2]

        return f"{var_type} {var_name} = {var_value};"
    
    def assign_stmt(self, items):
        var_name = items[0].value
        var_value = items[1]

        return f"{var_name} = {var_value};"
        
    def print_stmt(self, items):
        expr = items[0]
        return f'println!("{{}}", {expr});'
        
    def number(self, items):
        return items[0].value
    
    def string(self, items):
        str_value = items[0].value
        return f"{str_value}.to_string()"
    
    def var_name(self, items):
        return items[0].value
    
    def term(self, items):
        result = []
        for i in items:
            if hasattr(i, 'value'):
                result.append(i.value)
            else:
                result.append(str(i))
        return " ".join(result)

    def factory(self, items):
        result = []
        for i in items:
            if hasattr(i, 'value'):
                result.append(i.value)
            else:
                result.append(str(i))
        return " ".join(result)
    
    def int_num(self, items):
        return items[0].value
    
    def float_num(self, items):
        return items[0].value