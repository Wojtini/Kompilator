from register import REG
from misc.identifier import ArrayAccess
from misc.jumps import *
# pobrana liczbe zapisuje w rejestrze r_a oraz k <- k + 1
def GET(p):
    p.makeInstr('GET')

#wyswietla zawartosc rejestru r_a oraz k <- k + 1
def PUT(p):
    p.makeInstr('PUT')

def LOAD(p,regX):
    p.makeInstr(f'LOAD {regX}')

def STORE(p,regX):
    p.makeInstr(f'STORE {regX}')

def ADD(p,regX):
    p.makeInstr(f'ADD {regX}')

def SUB(p,regX):
    p.makeInstr(f'SUB {regX}')

def SHIFT(p, regX):
    p.makeInstr(f'SHIFT {regX}')

def SWAP(p, regX):
    # if regX == REG.A:
    #     raise Exception("Swapping with Reg A (Are you debil?)")
    p.makeInstr(f'SWAP {regX}')

def RESET(p, regX):
    p.makeInstr(f'RESET {regX}')

def INC(p, regX):
    p.makeInstr(f'INC {regX}')

def DEC(p,x):
    raise Exception("not implemented")

def JUMP(p,j):
    raise Exception("Are you sure u want to use this")

def JPOS(p,x):
    raise Exception("Are you sure u want to use this")

def JZERO(p,j):
    raise Exception("Are you sure u want to use this")

def JNEG(p,x):
    raise Exception("Are you sure u want to use this")

################
### COMMANDS ###
################

# DZIALA - wykorzystuje REG.A i REG.B, REG.G w przypadku tablic
def READ(p, pid):
    pid.memAddressToReg(p, REG.B, REG.G) #Zaladuj miejsce w pamieci do REG.B
    GET(p) # dostan wartosc w REG.A
    STORE(p, REG.B) # storujemy REG.A tam gdzie REG.B wskazuje
    
    
# DZIALA
def WRITE(p, val):
    val.evalToRegInstr(p, REG.B) #Laduje val
    SWAP(p,REG.B) #dajemy do A zeby wyprintowac
    PUT(p)
    # PRINT_ALL_REG(p) 
# DZIALA
def ASSIGN(p, identifier, expression):
    decl = identifier.declaration
    if decl.islocal:
        raise Exception("Trying to modify local variable '%s'" % decl.pidentifier)
    if not isinstance(identifier, ArrayAccess) and decl.isarr == True:
        raise Exception("'%s' is an array, but used as normal variable" % decl.pidentifier)

    
    # TO DOKO
    expression.evalToRegInstr(p, REG.C) #jest git w REG.C wartosc
    #(dziala dla number i pid'a)

    identifier.memAddressToReg(p, REG.B, REG.G)
    SWAP(p, REG.C)

    STORE(p, REG.B)

##################
### ARYTMETYKA ###
##################

# DZIALA
def PLUS(p, leftValue, rightValue, destReg=REG.B, helpReg=REG.D):
    if destReg == helpReg:
        raise Exception("Cannot use same registers")
    leftValue.evalToRegInstr(p, destReg)
    rightValue.evalToRegInstr(p, helpReg)
    SWAP(p, destReg)
    ADD(p, helpReg)
    SWAP(p, destReg)

# DZIALA
def MINUS(p, leftValue, rightValue, destReg=REG.B, helpReg=REG.D):
    if destReg == helpReg:
        raise Exception("Cannot use same registers")
    leftValue.evalToRegInstr(p, destReg)
    rightValue.evalToRegInstr(p, helpReg)
    SWAP(p, destReg)
    SUB(p, helpReg)
    SWAP(p, destReg)

# NIE DZIALA MOZLIWOSC OPTYMALIZACJI
def TIMES(p, leftValue, rightValue, destReg=REG.B, helpReg=REG.D):
    raise Exception("TIMES NOT IMPLEMENTED YET")
    if destReg == helpReg:
        raise Exception("Cannot use same registers")
    leftValue.evalToRegInstr(p, destReg)
    rightValue.evalToRegInstr(p, helpReg)
def DIV(p, leftValue, rightValue, destReg=REG.B, helpReg=REG.D):
    raise Exception("DIV NOT IMPLEMENTED YET")
def MOD(p, leftValue, rightValue, destReg=REG.B, helpReg=REG.D):
    raise Exception("MOD NOT IMPLEMENTED YET")

###############
### WARUNKI ###
###############

# DZIALA zmienne + number
def IF_THEN(p, cond, thenCommands):
    cond.generateCode(p)
    futureJZERO = FutureJZERO(p) #Przeskakuje jumpa (dom. 2)
    futureJUMP = FutureJUMP(p) #Przeskakuje do ENDIF

    thenId = p.getCounter()
    for command in thenCommands:
        command.generateCode(p)
    endId = p.getCounter()

    futureJZERO.finish(thenId)
    futureJUMP.finish(endId)

def IF_THEN_ELSE(p, cond, thenCommands, elseCommands):
    cond.generateCode(p)
    jumpIfTrue = FutureJZERO(p)
    jumpIfFalse = FutureJUMP(p)

    thenId = p.getCounter()

    for command in thenCommands:
        command.generateCode(p)

    skipElseIfTrue = FutureJUMP(p)

    elseId = p.getCounter()

    for command in elseCommands:
        command.generateCode(p)

    endId = p.getCounter()

    jumpIfTrue.finish(thenId)
    jumpIfFalse.finish(elseId)
    skipElseIfTrue.finish(endId)

##################
### CONDITIONS ###
##################

def CONDITION_EQ(p, leftVal, rightVal):
    leftVal.evalToRegInstr(p, REG.B)  
    rightVal.evalToRegInstr(p, REG.C)   
    SWAP(p, REG.B)
    SUB(p, REG.C)
    # 0 if true
    # everything else if false

def CONDITION_NEQ(p, leftVal, rightVal):
    CONDITION_EQ(p, leftVal, rightVal)

    yesZeroJump = FutureJZERO(p) #Jesli zero w rejestrze
    
    #Jesli nie zero
    RESET(p, REG.A)
    skipJump = FutureJUMP(p)

    yesZeroJumpId = p.getCounter()
    #jesli zero
    INC(p, REG.A)

    skipJumpId = p.getCounter()
    skipJump.finish(skipJumpId)
    yesZeroJump.finish(yesZeroJumpId)

# Uproscic Jumpy...
def CONDITION_GE(p, leftVal, rightVal):
    leftVal.evalToRegInstr(p, REG.B) #wieksza 
    rightVal.evalToRegInstr(p, REG.C)

    SWAP(p, REG.B)
    SUB(p, REG.C)

    jumpZero = FutureJZERO(p)   # jesli zero 
    jumpNeg = FutureJNEG(p)     # jesli ujemne

    # jesli REG.A = REG.B - REG.C > 0
    RESET(p, REG.A)         # ustaw na zero
    jumpEnd = FutureJUMP(p) # i tyle


    # jesli REG.A = 0
    jumpZero.finish(p.getCounter())
    INC(p, REG.A)

    # jesli REG.A < 0
    # nic nie rob
    jumpEnd.finish(p.getCounter())
    jumpNeg.finish(p.getCounter())

def CONDITION_GEQ(p, leftVal, rightVal):
    leftVal.evalToRegInstr(p, REG.B) #wieksza 
    rightVal.evalToRegInstr(p, REG.C)

    SWAP(p, REG.B)
    SUB(p, REG.C)

    jumpPos = FutureJNEG(p)

    # jesli REG.A = REG.B - REG.C > 0
    RESET(p, REG.A)

    jnegID = p.getCounter()
    jumpPos.finish(jnegID)

    # jesli REG.A < 0
    # nic nie rob

def CONDITION_LE(p, leftVal, rightVal):
    CONDITION_GE(p, rightVal, leftVal)

def CONDITION_LEQ(p, leftVal, rightVal):
    CONDITION_GEQ(p, rightVal, leftVal)

###############
### HELPERS ###
###############

# Ustawia podana wartosc w REG.A i podstawia pod REG.X
def setValueOfRegister(p, regX, val):
    RESET(p, REG.A)
    # print(f"KRUWA {val}")
    binVal = bin(val)[2:]   # na binarny
    length = len(binVal)
    
    for i, digit in enumerate(binVal):
        if digit == '1':
            INC(p, REG.A)
        if i < length - 1:
            SHIFT(p, REG.H) #shiftujemy o 2^reg.H (gdzie reg.H = 1 CONSTANT)

    SWAP(p, regX)


# Uzywa A i wybrany rejestr / laduje do reg wartosc zmiennej
def LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, identifier, reg):
    decl = identifier.declaration

    if reg == REG.A:
        raise Exception("Cant use store identifier value in REG.A '%s'" % reg)
    if decl.isarr == True:
        raise Exception("'%s' is an array, but accessed as normal variable" % decl.pidentifier)
    
    identifier.memAddressToReg(p, reg, None)

    LOAD(p, reg)

    SWAP(p, reg)

# Laduje wartosc zmiennej w tablicy do wybranego rejestru
def LOAD_ARRAY_VALUE_TO_REGISTER(p, identifier, reg):
    identifier.memAddressToReg(p, reg, REG.G)
    LOAD(p, reg)
    SWAP(p, reg)
    
def LOAD_NUMBER_VALUE_TO_REGISTER(p, number, reg): # reg ignorowane
    number = int(number)
    setValueOfRegister(p, reg, number) #odrazu wartosc w REG.A laduje
    # PRINT_ALL_REG(p)

def PRINT_ALL_REG(p):
    PUT(p)

    SWAP(p, REG.B)
    PUT(p)
    SWAP(p, REG.B)

    SWAP(p, REG.C)
    PUT(p)
    SWAP(p, REG.C)

    SWAP(p, REG.D)
    PUT(p)
    SWAP(p, REG.D)

    SWAP(p, REG.E)
    PUT(p)
    SWAP(p, REG.E)
    
    SWAP(p, REG.F)
    PUT(p)
    SWAP(p, REG.F)

    SWAP(p, REG.G)
    PUT(p)
    SWAP(p, REG.G)

    SWAP(p, REG.H)
    PUT(p)
    SWAP(p, REG.H)
