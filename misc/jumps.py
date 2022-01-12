from register import REG
from Memory import manager as MemoryManager

class Future:
    def finish(self, i):
        raise Exception("Future finish not yet defined for %s" % self.__class__)

class FutureJZERO(Future):
    def __init__(self, program):
        self.program = program
        self.instrId = program.addFutureInstr("FUTURE JZERO")
        
    def finish(self, j):
        self.program.instructions[self.instrId] = f"JZERO {j - self.instrId}"

class FutureJUMP(Future):
    def __init__(self, program):
        self.program = program
        self.instrId = program.addFutureInstr("FUTURE JUMP")
        
    def finish(self, j):
        self.program.instructions[self.instrId] = f"JUMP {j-self.instrId}"

class FutureJPOS(Future):
    def __init__(self, program):
        self.program = program
        self.instrId = program.addFutureInstr("FUTURE JPOS")
        
    def finish(self, j):
        self.program.instructions[self.instrId] = f"JPOS {j-self.instrId}"

class FutureJNEG(Future):
    def __init__(self, program):
        self.program = program
        self.instrId = program.addFutureInstr("FUTURE JNEG")
        
    def finish(self, j):
        self.program.instructions[self.instrId] = f"JNEG {j-self.instrId}"