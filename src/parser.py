from lark import Lark

crest_grammar = r"""
    // --- ТОКЕНЫ (Используем /.../ для регулярок) ---
    DOTDOT: ".."
    VAL: "val"
    VAR: "var"
    AND: "and"
    OR: "or"
    TYPE: "int" | "float" | "str" | "bool"
    
    // Регулярки теперь внутри /.../
    FLOAT: /\d+\.\d+/
    INT: /\d+/
    NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
    
    PLUS: "+"
    MINUS: "-"
    MUL: "*"
    DIV: "/"

    COMMENT: /\/\/.*/
    
    LOGIC_OP: AND | OR
    COMPARE_OP: "==" | "!=" | ">" | "<" | ">=" | "<="

    // --- СТРУКТУРА ---
    start: statement+
    ?statement: var_decl | assign_stmt | print_stmt | if_stmt | while_stmt | for_stmt | fn_stmt| return_stmt | fn_call_stmt | method_call_stmt

    block: "{" statement+ "}"

    if_stmt: "if" condition block ["else" block]
    while_stmt: "while" condition block
    for_stmt: "for" NAME "in" expression DOTDOT expression block

    param: NAME ":" TYPE
    params: param ("," param)*

    fn_stmt: "fn" NAME "(" [params] ")" ["->" TYPE] block
    return_stmt: "return" expression

    arguments: expression ("," expression)*

    fn_call: NAME "(" [arguments] ")"
    fn_call_stmt: fn_call

    method_call: NAME "." NAME "(" [arguments] ")"
    method_call_stmt: method_call

    condition: (expression | COMPARE_OP | LOGIC_OP)+

    var_decl: (VAL | VAR) NAME ":" TYPE "=" expression -> decl_with_type 
            | (VAL | VAR) NAME "=" expression          -> decl_no_type

    assign_stmt: NAME "=" expression

    print_stmt: "print" "(" expression ")"

    list_expr: "[" [arguments] "]"

    // --- МАТЕМАТИКА ---
    ?expression: term
    ?term: factory ((PLUS | MINUS) factory)*
    ?factory: atom ((MUL | DIV) atom)*
    ?atom: FLOAT  -> float_num
        | INT    -> int_num
        | STRING -> string
        | method_call
        | fn_call
        | list_expr
        | NAME   -> var_name

    ESCAPED_STRING: /"[^"]*"/
    STRING: ESCAPED_STRING
    
    %import common.WS
    %ignore WS
    %ignore COMMENT
"""

def get_parse():
    return Lark(crest_grammar, start='start', parser='lalr', propagate_positions=True)

def parse_code(code_text):
    parser = get_parse()
    return parser.parse(code_text)