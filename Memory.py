class MemoryManager:
    def __init__(self):
        self.declarations = None
        self.declaredPidentifiers = set()
        self.memmap = {}
        self.lastblockid = 9

    def checkMemory(self, declarations):
        self.declarations = declarations
        self.checkDuplicateDeclarations()

    def checkDuplicateDeclarations(self):
        for decl in self.declarations:
            pidentifier = decl.pidentifier
            if pidentifier in self.declaredPidentifiers:
                raise Exception("Duplicate declaration for '%s' at line %i" % (pidentifier, decl.lineNumber))
            self.declaredPidentifiers.add(pidentifier)
    
    def unregister(self, declaration):
        try:
            del self.memmap[declaration.pidentifier]
            declaration.memoryId = None
        except KeyError as key:
            raise Exception("Trying to unregister not declared identifier %s" % key)

    def assignMemToVariables(self):
        for declaration in self.declarations:
            self.assignMem(declaration)

    def assignMem(self, declaration):
        pidentifier = declaration.pidentifier

        if pidentifier in self.memmap and self.memmap[pidentifier].memoryId != None:
            raise Exception(f"Duplicate memory allocation for {declaration}")

        blockLength = 1
        if declaration.isArray():
            blockLength = declaration.length

        assignedMemoryBlockId = self.lastblockid
        
        self.memmap[pidentifier] = declaration
        declaration.memoryId = assignedMemoryBlockId

        self.lastblockid += blockLength

    # def getUnnamedMemBlock(self):
    #     assignedMem = self.lastblockid
    #     self.lastblockid += 1
    #     return assignedMem

    def getSymbols(self):
        return self.memmap.keys()

    def getBlockId(self, name):
        try:
            memoryId = self.memmap[name].memoryId
            if memoryId == None:
                raise Exception("Identifier '%s' has no memory allocated" % name)
            return memoryId
        except KeyError:
            raise Exception("Identifier '%s' is not declared in current context" % name)

    def getVariableByPidentifier(self, pid):
        if pid not in self.memmap:
            raise Exception("Identifier '%s' is not declared in current context" % pid)

        decl = self.memmap[pid]
        if not decl:
            raise Exception("Declaration '%s' not found" % pid)
        return decl

manager = MemoryManager()