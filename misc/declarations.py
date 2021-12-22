from Memory import manager as MemoryManager

class DeclarationVar:
    def __init__(self, pidentifier, isarr = False, islocal = False, lineNumber = -1):
        self.pidentifier = pidentifier
        self.lineNumber = lineNumber
        self.memoryId = None
        self.isarr = isarr
        self.length = 1
        self.islocal = islocal
        self.initialized = False

    def delete(self):
        pass
        # MemoryManager.unregister(self)

    def register(self):
        self.initialized = True
        pass
        # MemoryManager.assignMem(self)

    def isArray(self):
        return self.isarr == True

    def __repr__(self):
        return str((self.pidentifier, self.memoryId, self.length, f"IsArray: {self.isArray()}"))

class DeclarationArray(DeclarationVar):
    def __init__(self, pidentifier, rangeFrom, rangeTo, line):
        super(DeclarationArray, self).__init__(pidentifier, True, lineNumber=line)
        if rangeFrom > rangeTo:
            raise Exception(f"Bad array range in declaration of {pidentifier}[{rangeFrom},{rangeTo}] in line {line}")
        self.rangeFrom = rangeFrom
        self.rangeTo = rangeTo
        self.length = rangeTo - rangeFrom + 1