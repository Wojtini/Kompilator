from ply import lex, yacc

tokens = (
    'VAR', 'BEGIN', 'END',
    'PLUS','MINUS','TIMES','DIV','MOD',
    'EQ','NEQ','LE','GE','LEQ','GEQ',
    'ASSIGN',
    'FOR','TO','DOWNTO', 'FROM', 'ENDFOR',
    'REPEAT', 'UNTIL',
    'READ','WRITE',
    'IF', 'THEN', 'ELSE', 'ENDIF',
    'WHILE', 'DO', 'ENDWHILE',
    'PIDENTIFIER',
    'NUM',
    'SEMICOLON', 'COLON', 'COMMA', 'LQBRACKET', 'RQBRACKET'
)

t_ignore = ' \t'
t_ignore_COMMENT = '\([A-Za-z0-9\;\[\] \\\n]*\)'

t_VAR = r'VAR'
t_BEGIN = r'BEGIN'
t_END = r'END'

t_PIDENTIFIER = r'[_a-z]+'
t_NUM = r'-?\d+'

t_PLUS = r'PLUS'
t_MINUS = r'MINUS'
t_TIMES = r'TIMES'
t_DIV = r'DIV'
t_MOD = r'MOD'

t_EQ = r'EQ'
t_NEQ = r'NEQ'
t_LE = r'LE'
t_GE = r'GE'
t_LEQ = r'LEQ'
t_GEQ = r'GEQ'

t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_ENDIF = r'ENDIF'

t_WHILE = r'WHILE'
t_DO = r'DO'
t_ENDWHILE = r'ENDWHILE' 

t_ASSIGN = r'ASSIGN'

t_FOR = r'FOR'
t_FROM = r'FROM'
t_TO = r'TO'
t_DOWNTO = r'DOWNTO'
t_ENDFOR = r'ENDFOR'

t_REPEAT = r'REPEAT'
t_UNTIL = r'UNTIL'

t_READ = r'READ'
t_WRITE = r'WRITE'

t_SEMICOLON = r'[;]'
t_COLON = r'[:]'
# t_LBRACKET = r'\('
# t_RBRACKET = r'\)'
t_LQBRACKET = r'\['
t_RQBRACKET = r'\]'
t_COMMA = r'\,'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Compilation failed")
    print(f"Illegal character {t.value[0]} at line {t.lineno}")
    exit(0)

# reserved_re = '|'.join(reserved.values())
# @TOKEN(reserved_re)
# def t_CONTROL(t):
#     controlToken = reserved.get(t.value)
#     if(not controlToken):
#         raise SyntaxError("Bad control sequence '%s'" % t.value)
#     t.type = controlToken
#     return t