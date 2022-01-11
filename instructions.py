from register import REG
from misc.identifier import ArrayAccess
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

def JUMP(p,x):
    raise Exception("not implemented")

def JPOS(p,x):
    raise Exception("not implemented")

def JZERO(p,x):
    raise Exception("not implemented")

def JNEG(p,x):
    raise Exception("not implemented")

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
