from ply import lex, yacc

import lexer
import parser
import sys
# 9    a
# 10    b
# 11    c
# 12  tab 1
# 13  tab 2
# 14  tab 3
# 15  tab 4
# 16  tab 5
# data = '''
#     VAR
#         a, b
#     BEGIN
#         a ASSIGN 1;
#         b ASSIGN 10;
#         FOR i FROM a TO b DO
#             WRITE i;
#             b ASSIGN b MINUS 1;
#         ENDFOR
#     END
# '''
# data1 = '''
#     VAR
#  n , p
#  BEGIN
#  READ n ;
#  IF n GEQ 0 THEN
#  REPEAT
#  p ASSIGN n DIV 2;
#  p ASSIGN 2 TIMES p ;
#  IF n NEQ p THEN
#  WRITE 1;
#  ELSE
#  WRITE 0;
#  ENDIF
#  n ASSIGN n DIV 2;
#  UNTIL n EQ 0;
#  ENDIF
#  END
# '''
# data2 = '''
#     VAR
#         n , m , reszta , potega , dzielnik
#     BEGIN
#         READ n ;
#         dzielnik ASSIGN 2;
#         m ASSIGN dzielnik TIMES dzielnik ;
#         WHILE n GEQ m DO
#             potega ASSIGN 0;
#             reszta ASSIGN n MOD dzielnik ;
#             WHILE reszta EQ 0 DO
#                 n ASSIGN n DIV dzielnik ;
#                 potega ASSIGN potega PLUS 1;
#                 reszta ASSIGN n MOD dzielnik ;
#             ENDWHILE
#             IF potega GE 0 THEN ( czy znaleziono dzielnik )
#                 WRITE dzielnik ;
#                 WRITE potega ;
#             ELSE
#                 dzielnik ASSIGN dzielnik PLUS 1;
#                 m ASSIGN dzielnik TIMES dzielnik ;
#             ENDIF
#         ENDWHILE
#         IF n NEQ 1 THEN ( ostatni dzielnik )
#             WRITE n ;
#             WRITE 1;
#         ENDIF
#     END
# '''



lexer = lex.lex(module=lexer, debug=0)
parser = yacc.yacc(module=parser)

filename = sys.argv[1]

output = filename.split('.')
output[2] = 'mg'
output = '.'.join(output)


data = ''

with open(sys.argv[1]) as f:
    data = f.read()

lexer.input(data)

program = parser.parse(data, lexer=lexer)



with open(output, 'w') as f:
    f.write(program.commandsToText())
