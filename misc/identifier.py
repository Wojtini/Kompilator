from Memory import manager as MemoryManager
import instructions
from register import REG

class Identifier:
    def __init__(self, pidentifier):
        self.pidentifier = pidentifier

    @property
    def declaration(self):
        return MemoryManager.getVariableByPidentifier(self.pidentifier)

    def memAddressToReg(self, p, reg1, reg2):
        memoryId = MemoryManager.getBlockId(self.pidentifier)
        instructions.setValueOfRegister(p, reg1, memoryId)

class ArrayAccess(Identifier):
    def __init__(self, pidentifier, index):
        super(ArrayAccess, self).__init__(pidentifier)
        self.index = index

    def memAddressToReg(self, p, reg1, reg2):
        raise Exception("Not defined")

class ArrayAccessByNum(ArrayAccess):
    def __init__(self, pidentifier, num):
        super(ArrayAccessByNum, self).__init__(pidentifier, num)

    def memAddressToReg(self, p, reg1, reg2):
        declaration = self.declaration

        if not declaration.isArray():
            raise Exception("'%s' is not an Array" % declaration.pidentifier)

        memoryId = MemoryManager.getBlockId(self.pidentifier)
        arrRangeFrom = declaration.rangeFrom
        arrRangeTo = declaration.rangeTo
        offset = int(self.index) - arrRangeFrom
        if offset < 0 :
            raise Exception("Array out of bounds. Given %i, but range is (%i:%i)" % (self.index, arrRangeFrom, arrRangeTo))
        
        trueId = memoryId + offset
        instructions.setValueOfRegister(p, reg1, trueId)

        # instructions.PRINT_ALL_REG(p)



class ArrayAccessByPidentifier(ArrayAccess):
    def __init__(self, pidentifier, pid):
        super(ArrayAccessByPidentifier, self).__init__(pidentifier, pid)

    def memAddressToReg(self, p, reg1, reg2):
        declaration = self.declaration

        if not declaration.isArray():
            raise Exception("'%s' is not an Array" % declaration.pidentifier)
        if reg2 == None:
            raise Exception("Register for variable not specified while accessing array via Variable")
        memoryId = declaration.memoryId
        arrRangeFrom = declaration.rangeFrom
        arrRangeTo = declaration.rangeTo
        # print(arrRangeFrom)
        # print(arrRangeTo)
        # print(declaration)
        # print(self.index)

        #   tab[1:5]
        #   value = 3
        #   tab[value]
        
        instructions.LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, Identifier(self.index) , reg2)    # reg2 = value / 3

        instructions.setValueOfRegister(p, reg1, arrRangeFrom)                        # reg1 = arrRangeFrom / 1

        instructions.SWAP(p, reg2)                                                  #value >>> regA

        instructions.SUB(p, reg1)                                                  # regA = regA - reg1 (value - arrRangeFrom)
        #                                                                            # regA = 3 - 1 = 2  (offset)
                                                                                   
        instructions.SWAP(p, reg2)                                                  # offset >>> reg2

        instructions.setValueOfRegister(p, reg1, memoryId)                            # reg1 = memoryId
        instructions.SWAP(p, reg1)

        instructions.ADD(p, reg2)                                                   # regA = regA + regB // memoryid + offset
        instructions.SWAP(p, reg1)                                                  # regB = regA
        
  

        # p.makeInstr("")
        # instructions.PUT(p)
        # instructions.PUT(p)
        # instructions.PUT(p)


