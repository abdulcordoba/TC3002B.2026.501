grammar RaraLang;

prog
    : stat* EOF
    ;

stat
    : ID ASSIGN expr       # AssignStat
    | PRINT printArg       # PrintStat
    ;

printArg
    : STRING               # StringPrintArg
    | expr                 # ExprPrintArg
    ;

expr
    : '(' expr ')'         # ParenExpr
    | literal              # LiteralExpr
    | ID                   # VarExpr
    | NEG expr             # NegExpr
    | expr (MUL | DIV) expr # MulDivExpr
    | expr DOUBLE_PLUS expr # DoublePlusExpr
    | expr MOD expr        # ModExpr
    | expr AVG expr        # AvgExpr
    | expr (PLUS | MINUS) expr # AddSubExpr
    ;

literal
    : INT
    | BASED_INT
    ;

ASSIGN
    : '<--'
    ;

PRINT
    : 'print'
    ;

MUL
    : '×'
    ;

DIV
    : '÷'
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

MOD
    : '⊞'
    ;

DOUBLE_PLUS
    : '⊠'
    ;

AVG
    : '≈'
    ;

NEG
    : '±'
    ;

INT
    : [0-9]+
    ;

BASED_INT
    : '[' [0-9A-Fa-f]+ ':' [0-9]+ ']'
    ;

STRING
    : '"' ( '\\' . | ~["\\\r\n] )* '"'
    ;

ID
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

LINE_COMMENT
    : '#' ~[\r\n]* -> skip
    ;
