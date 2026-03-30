from lark import Lark

crest_grammar = r"""
    // --- ТОКЕНЫ ---
    DOTDOT: ".."
    VAL: "val"
    VAR: "var"
    AND: "and"
    OR: "or"
    TYPE: "int" | "float" | "str" | "bool"
    
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
    ?statement: var_decl | assign_stmt | print_stmt | if_stmt | while_stmt | for_stmt | fn_stmt | return_stmt | fn_call_stmt | method_call_stmt | class_stmt

    block: "{" statement+ "}"

    class_var: (VAL | VAR) NAME ":" TYPE
    class_stmt: "class" NAME "{" (class_var | fn_stmt)* "}"

    if_stmt: "if" expression block ["else" block]
    while_stmt: "while" expression block
    for_stmt: "for" NAME "in" expression DOTDOT expression block

    param: NAME ":" TYPE | VAR NAME | NAME
    params: param ("," param)*
    fn_stmt: "fn" NAME "(" [params] ")" ["->" TYPE] block
    return_stmt: "return" expression

    arguments: expression ("," expression)*
    fn_call: NAME "(" [arguments] ")"
    fn_call_stmt: fn_call

    method_call: NAME "." NAME "(" [arguments] ")"
    method_call_stmt: method_call

    prop_access: NAME "." NAME

    var_decl: (VAL | VAR) NAME ":" TYPE "=" expression -> decl_with_type 
            | (VAL | VAR) NAME "=" expression          -> decl_no_type

    assign_stmt: NAME "=" expression
    print_stmt: "print" "(" expression ")"

    list_expr: "["[arguments] "]"
    
    dict_item: expression ":" expression
    dict_items: dict_item ("," dict_item)*
    dict_expr: "{" [dict_items] "}"

    index_expr: NAME "[" expression "]"

    // --- ВЫРАЖЕНИЯ, ЛОГИКА И МАТЕМАТИКА ---
    ?expression: condition
    
    ?condition: cmp_expr (LOGIC_OP cmp_expr)*
    ?cmp_expr: math_expr (COMPARE_OP math_expr)* | math_expr
    
    ?math_expr: term
    ?term: factor ((PLUS | MINUS) factor)*
    ?factor: atom ((MUL | DIV) atom)*
    
    ?atom: FLOAT  -> float_num
        | INT    -> int_num
        | STRING -> string
        | method_call
        | prop_access
        | fn_call
        | list_expr
        | dict_expr
        | index_expr
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