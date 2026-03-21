from lark import Lark

crest_grammar = """
    VAL: "val"
    VAR: "var"
    NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
    COMPARE_OP: "==" | "!=" | ">" | "<" | ">=" | "<="

    start: statement+
    ?statement: var_decl | print_stmt | if_stmt
    
    block: "{" statement+ "}"
    if_stmt: "if" condition block ["else" block]

    var_decl: (VAL | VAR) NAME ":" NAME "=" expression -> decl_with_type 
            | (VAL | VAR) NAME "=" expression          -> decl_no_type

    print_stmt: "print" "(" expression ")"

    ?condition: expression COMPARE_OP expression

    ?expression: term
    ?term: factory (("+" | "-") factory)*
    ?factory: atom (("*" | "/") atom)*
    ?atom: NUMBER -> number 
        | STRING -> string 
        | NAME   -> var_name

    %import common.SIGNED_NUMBER -> NUMBER
    %import common.ESCAPED_STRING -> STRING
    %import common.WS
    %ignore WS
"""

def get_parse():
    return Lark(crest_grammar, start='start', parser='lalr', propagate_positions=True)

def parse_code(code_text):
    parser = get_parse()
    return parser.parse(code_text)