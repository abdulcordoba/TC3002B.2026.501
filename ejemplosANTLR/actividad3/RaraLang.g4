grammar RaraLang;

prog
    : item* EOF
    ;

item
    : funcDef
    | stat
    ;

stat
    : ID ASSIGN expr       # AssignStat
    | PRINT printArg       # PrintStat
    | IF expr block (ELSE block)? # IfStat
    | WHILE expr block     # WhileStat
    | RETURN expr          # ReturnStat
    ;

funcDef
    : FUNC ID '(' ')' block
    ;

block
    : '{' stat* '}'
    ;

printArg
    : STRING               # StringPrintArg
    | expr                 # ExprPrintArg
    ;

expr
    : '(' expr ')'         # ParenExpr
    | literal              # LiteralExpr
    | ID '(' ')'           # CallExpr
    | ID                   # VarExpr
    | NEG expr             # NegExpr
    | expr (MUL | DIV) expr # MulDivExpr
    | expr DOUBLE_PLUS expr # DoublePlusExpr
    | expr MOD expr        # ModExpr
    | expr AVG expr        # AvgExpr
    | expr (PLUS | MINUS) expr # AddSubExpr
    | expr (EQ | NE | LE | GE | LT | GT) expr # CompareExpr
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

IF
    : 'if'
    ;

ELSE
    : 'else'
    ;

WHILE
    : 'while'
    ;

FUNC
    : 'func'
    ;

RETURN
    : 'return'
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

EQ
    : '=='
    ;

NE
    : '!='
    ;

LE
    : '<='
    ;

GE
    : '>='
    ;

LT
    : '<'
    ;

GT
    : '>'
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
