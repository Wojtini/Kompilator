import instructions
from misc.identifier import ArrayAccess

class Expression:
    def evalToRegInstr(self, p, reg):
        raise Exception("evalToRegInstr() not defined for %s" % self.__class__)


class Number(Expression):
    def __init__(self, num):
        self.num = num

    def evalToRegInstr(self, p, reg):
        return instructions.LOAD_NUMBER_VALUE_TO_REGISTER(p, self.num, reg)


class ValueFromIdentifier(Expression):
    def __init__(self, identifier, lineNumber=-1):
        self.identifier = identifier
        self.lineNumber = lineNumber

    def evalToRegInstr(self, p, reg):
        try:
            isInitialized = self.identifier.declaration.initialized
            if isInitialized == False:
                raise Exception("Variable '%s' is not initialized" % self.identifier.pidentifier)
            if isinstance(self.identifier, ArrayAccess):
                return instructions.LOAD_ARRAY_VALUE_TO_REGISTER(p, self.identifier, reg)
            return instructions.LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, self.identifier, reg)
        except Exception as err:
            raise Exception(str(err) + " at line %i" % self.lineNumber)


class BinaryOperator(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evalToRegInstr(self, p, reg):
        if self.operator == 'PLUS':
            return instructions.PLUS(p, self.left, self.right, reg)
        elif self.operator == 'MINUS':
            return instructions.MINUS(p, self.left, self.right, reg)
        elif self.operator == 'TIMES':
            return instructions.TIMES(p, self.left, self.right, reg)
        elif self.operator == 'DIV':
            return instructions.DIV(p, self.left, self.right, reg)
        elif self.operator == 'MOD':
            return instructions.MOD(p, self.left, self.right, reg)
        else:
            raise Exception("Operator '%s' not defined" % self.operator)