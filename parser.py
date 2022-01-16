from ply.yacc import YaccProduction
from lexer import tokens
import misc.declarations as declarations
import misc.condition as conditions
import misc.commands as commands
import misc.identifier as identifier
import misc.expression as expression
from program import Program

precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIV', 'MOD'),
    )
###############
### PROGRAM ###
###############

def p_program_var(p):
    '''program : VAR declarations BEGIN commands END'''
    variables = p[2]
    commands = p[4]
    p[0] = Program(variables,commands)
    
def p_program(p):
    '''program : BEGIN commands END'''
    commands = p[2]
    p[0] = Program([], commands)

##################
### DEKLARACJE ###
##################

# def p_declarations_all(p):
#     '''declarations : declarations COMMA PIDENTIFIER
#     | declarations COMMA PIDENTIFIER LQBRACKET NUM COLON NUM RQBRACKET
#     | PIDENTIFIER
#     | PIDENTIFIER LQBRACKET NUM COLON NUM RQBRACKET
#     '''

def p_declarations_next(p):
    'declarations : declarations COMMA PIDENTIFIER'
    var = declarations.DeclarationVar(p[3],False,False,p.lineno(3))
    p[1].append(var)
    p[0] = p[1]
    

def p_declarations_array_next(p):
    'declarations : declarations COMMA PIDENTIFIER LQBRACKET NUM COLON NUM RQBRACKET'
    var = declarations.DeclarationArray(p[3],p[5],p[7],p.lineno(3))
    p[1].append(var)
    p[0] = p[1]

def p_declarations(p):
    'declarations : PIDENTIFIER'
    var = declarations.DeclarationVar(p[1],False,False,p.lineno(1))
    p[0] = []
    p[0].append(var)

def p_declarations_array(p):
    'declarations : PIDENTIFIER LQBRACKET NUM COLON NUM RQBRACKET'
    var = declarations.DeclarationArray(p[1],p[3],p[5],p.lineno(1))
    p[0] = []
    p[0].append(var)
    
################
### COMMANDS ###
################

# def p_commands_all(p):
#     '''commands : command
#                 | commands command'''

def p_commands_start(p):
    'commands : command'
    p[0] = [p[1]]

def p_commands_next(p):
    'commands : commands command'
    if not p[1]:
        p[1] = []
    p[1].append(p[2])
    p[0] = p[1]
    

###############
### COMMAND ###
###############


# def p_command_all(p):
#     ''' command : identifier ASSIGN expression SEMICOLON
#         | IF condition THEN commands ELSE commands ENDIF
#         | IF condition THEN commands ENDIF
#         | WHILE condition DO commands ENDWHILE
#         | REPEAT commands UNTIL condition SEMICOLON
#         | FOR PIDENTIFIER FROM value TO value DO commands ENDFOR
#         | FOR PIDENTIFIER FROM value DOWNTO value DO commands ENDFOR
#         | READ identifier SEMICOLON
#         | WRITE value SEMICOLON
#     '''

def p_command_assign(p):
    'command : identifier ASSIGN expression SEMICOLON'
    p[0] = commands.CommandAssign(p[1], p[3], p.lineno(2))
def p_command_ifthenelse(p):
    'command : IF condition THEN commands ELSE commands ENDIF'
    cond = p[2]
    thenCommands = p[4]
    elseCommands = p[6]
    p[0] = commands.CommandIfThenElse(p.lineno(1),cond,thenCommands,elseCommands)
def p_command_ifthen(p):
    'command : IF condition THEN commands ENDIF'
    cond = p[2]
    thenCommands = p[4]
    p[0] = commands.CommandIfThen(p.lineno(1),cond,thenCommands)
def p_command_whiledo(p):
    'command : WHILE condition DO commands ENDWHILE'
    cond = p[2]
    whileCommands = p[4]
    p[0] = commands.CommandWhileDo(p.lineno(1), cond, whileCommands)
def p_command_repeatuntil(p):
    'command : REPEAT commands UNTIL condition SEMICOLON'
    p[0] = commands.CommandRepeatUntil(p.lineno(1), p[2], p[4])
def p_command_forfromtodo(p):
    'command : FOR PIDENTIFIER FROM value TO value DO commands ENDFOR'
    p[0] = commands.CommandForFromToDo(p.lineno(1), p[2], p[4], p[6], p[8])
def p_command_forfromdowntodo(p):
    'command : FOR PIDENTIFIER FROM value DOWNTO value DO commands ENDFOR'
    p[0] = commands.CommandForFromDowntoDo(p.lineno(1), p[2], p[4], p[6], p[8])
def p_command_read(p):
    'command : READ identifier SEMICOLON'
    p[0] = commands.CommandRead(p.lineno(1), p[2])
def p_command_write(p):
    'command : WRITE value SEMICOLON'
    p[0] = commands.CommandWrite(p.lineno(1), p[2])


##################
### EXPRESSION ###
##################

def p_expression_empty(p):
    '''expression : value'''
    p[0] = p[1]

def p_expression_all(p):
    '''expression : value PLUS value
    | value MINUS value
    | value TIMES value
    | value DIV value
    | value MOD value
    '''
    p[0] = expression.BinaryOperator(p[1],p[2],p[3])
    
#################
### CONDITION ###
#################

def p_condition(p):
    '''condition : value EQ value
                | value NEQ value
                | value LE value
                | value GE value
                | value LEQ value
                | value GEQ value
    '''
    p[0] = conditions.Condition(p[1],p[2],p[3])

##############
### VALUES ###
##############

def p_value_number(p):
    '''value : NUM'''
    p[0] = expression.Number(p[1])

def p_value_identifier(p):
    '''value : identifier'''
    p[0] = expression.ValueFromIdentifier(p[1])

######################
### P_Indentifiers ###
######################

# def p_identifier_all(p):
#     '''identifier : PIDENTIFIER
#     | PIDENTIFIER LQBRACKET PIDENTIFIER RQBRACKET
#     | PIDENTIFIER LQBRACKET NUM RQBRACKET'''

def p_identifier(p):
    '''identifier : PIDENTIFIER'''
    p[0] = identifier.Identifier(p[1])

def p_identifier_array_pid(p):
    '''identifier : PIDENTIFIER LQBRACKET PIDENTIFIER RQBRACKET'''
    p[0] = identifier.ArrayAccessByPidentifier(p[1], p[3])

def p_identifier_array_num(p):
    '''identifier : PIDENTIFIER LQBRACKET NUM RQBRACKET'''
    p[0] = identifier.ArrayAccessByNum(p[1], p[3])

    

def p_error(p):
    raise SyntaxError("Unexpected token '%s' at line %i" % (p.value, p.lineno))