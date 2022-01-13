from ply import lex, yacc

import lexer
import parser

# 9    a
# 10    b
# 11    c
# 12  tab 1
# 13  tab 2
# 14  tab 3
# 15  tab 4
# 16  tab 5
data = '''
VAR
    a,b,c, tab[601:605]
BEGIN
    b ASSIGN 5;
    a ASSIGN b MOD -2;
    WRITE a;
END
'''
data2 = '''
VAR
    a,b,c, tab[601:605]
BEGIN
    a ASSIGN 603;
    READ tab[a];
    WRITE tab[a];
    WRITE tab[603];
END
'''
data1 = '''
VAR
    a,b,c,d, tab[1:5]
BEGIN
    READ a;
    READ tab[a];
    WRITE a;
    WRITE tab[1];
    WRITE tab[a];
END
'''
data3 = '''
VAR
    a,b,c,d, tab[1:5]
BEGIN
    a ASSIGN 1;
    WRITE a;

    tab[1] ASSIGN 2;
    WRITE tab[1];

    b ASSIGN 2;
    tab[b] ASSIGN 3;
    WRITE tab[b];

    c ASSIGN 4;
    tab[3] ASSIGN c;
    WRITE tab[3];

    d ASSIGN 5;
    tab[d] ASSIGN d;
    WRITE tab[d];
END
'''

lexer = lex.lex(module=lexer, debug=0)
parser = yacc.yacc(module=parser)

lexer.input(data)

# Do pokazywania tokenow
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break
#     print(tok)

program = parser.parse(data, lexer=lexer)
