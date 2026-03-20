from lark import Transformer

class RustGen(Transformer):
    def start(self, statements):
        code = "\n".join(statements)
        return f"fn main() {{\n {code}\n}}"
    
    def var_decl(self, items):
        var_type = items[0].value
        var_name = items[1].value
        var_value = items[2]

        if var_type == "val":
            return f"let {var_name} = {var_value};"
        
        elif var_type == "var":
            return f"let mut {var_name} = {var_value};"
        
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