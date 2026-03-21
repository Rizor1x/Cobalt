from lark import Transformer
from error import CrestError

class RustGen(Transformer):
    def __init__(self, code, file_path):
        self.code = code
        self.file_path = file_path
        super().__init__()

    def start(self, statements):
        code = "\n    ".join(statements)
        return f"fn main() {{\n    {code}\n}}"
    
    def block(self, items):
        code = "\n    ".join(items)
        return f"{{\n    {code}\n}}"
    
    def condition(self, items):
        result = [getattr(i, 'value', str(i)) for i in items]
        return " ".join(result)

    def if_stmt(self, items):
        cond = items[0]
        if_block = items[1]
        
        if len(items) == 3:
            else_block = items[2]
            return f"if {cond} {if_block} else {else_block}"
        else:
            return f"if {cond} {if_block}"
    
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
        result =[getattr(i, 'value', str(i)) for i in items]
        return " ".join(result)

    def factory(self, items):
        result =[getattr(i, 'value', str(i)) for i in items]
        return " ".join(result)