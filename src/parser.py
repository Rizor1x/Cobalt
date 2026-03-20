from lark import Lark

crest_grammar = """
    start: statement+

    ?statement: var_decl | print_stmt

    var_decl: (VAL | VAR) NAME "=" expression

    print_stmt : "print" "(" expression ")"

    ?expression: NUMBER -> number | STRING -> string | NAME -> var_name

    VAL: "val"
    VAR: "var"

    // --- ВСТРОЕННЫЕ ПРАВИЛА LARK ---
    %import common.CNAME -> NAME
    %import common.SIGNED_NUMBER -> NUMBER
    %import common.ESCAPED_STRING -> STRING
    %import common.WS
    
    %ignore WS
"""

def get_parse():
    return Lark(crest_grammar, start='start', parser='lalr', lexer='basic')

def parse_code(code_text):
    parser = get_parse()
    return parser.parse(code_text)