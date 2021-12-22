from ply import lex, yacc

import lexer
import parser

# data = '''
# VAR
#     n, p, tab[20:40]
# BEGIN
#     READ n;
#     IF n GEQ 0 THEN
#         REPEAT
#             p ASSIGN n DIV 2;
#             p ASSIGN 2 TIMES p;
#             IF n NEQ p THEN
#                 WRITE 1;
#             ELSE
#                 WRITE 0;
#             ENDIF
#             n ASSIGN n DIV 2;
#         UNTIL n EQ 0;
#     ENDIF
# END
# '''

data = '''
VAR
    n
BEGIN
    READ n;
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
