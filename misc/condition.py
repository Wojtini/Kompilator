import instructions

class Condition:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def generateCode(self, p):
        if self.operator == 'GE':
            return instructions.CONDITION_GE(p, self.left, self.right)
        if self.operator == 'GEQ':
            return instructions.CONDITION_GEQ(p, self.left, self.right)
        if self.operator == 'LE':
            return instructions.CONDITION_LE(p, self.left, self.right)
        if self.operator == 'LEQ':
            return instructions.CONDITION_LEQ(p, self.left, self.right)
        if self.operator == 'EQ':
            return instructions.CONDITION_EQ(p, self.left, self.right)
        if self.operator == 'NEQ':
            return instructions.CONDITION_NEQ(p, self.left, self.right)
        else:
            raise Exception("Undefined CONDITION operator '%s'" % self.operator)