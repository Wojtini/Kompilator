import instructions

class Condition:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def generateCode(self, p):
        if self.operator == 'GE':
            return instructions.CONDITION_GE(p, self.left, self.right)
        elif self.operator == 'GEQ':
            return instructions.CONDITION_GEQ(p, self.left, self.right)
        elif self.operator == 'LE':
            return instructions.CONDITION_LE(p, self.left, self.right)
        elif self.operator == 'LEQ':
            return instructions.CONDITION_LEQ(p, self.left, self.right)
        elif self.operator == 'EQ':
            return instructions.CONDITION_EQ(p, self.left, self.right)
        elif self.operator == 'NEQ':
            return instructions.CONDITION_NEQ(p, self.left, self.right)
        else:
            raise Exception("Undefined CONDITION operator '%s'" % self.operator)

    def negate(self):
        if self.operator == 'GE':
            self.operator = 'LEQ'
        elif self.operator == 'GEQ':
            self.operator = 'LE'
        elif self.operator == 'LE':
            self.operator = 'GEQ'
        elif self.operator == 'LEQ':
            self.operator = 'GE'
        elif self.operator == 'EQ':
            self.operator = 'NEQ'
        elif self.operator == 'NEQ':
            self.operator = 'EQ'
        else:
            raise Exception("Undefined CONDITION operator '%s'" % self.operator)
