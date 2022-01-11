import instructions

class Command:
    def __init__(self, line_number):
        self.line_number = line_number
        pass

    def generateCode(self, program):
        print(f"Generate Code not defined for {self.__class__}")

class CommandAssign(Command):
    def __init__(self, identifier, expression, line_number):
        super().__init__(line_number=line_number)
        self.identifier = identifier
        self.expression = expression
        pass

    def generateCode(self, p):
        self.identifier.declaration.initialized = True
        try:
            return instructions.ASSIGN(p, self.identifier, self.expression)
        except Exception as err:
            raise Exception('someting wong')
            # raise Exception(str(err) + " at line %i" % self.line_number)


class CommandIfThenElse(Command):
    def __init__(self, line_number, condition, thenCommands, elseCommands):
        super().__init__(line_number=line_number)
        self.condition = condition
        self.thenCommands = thenCommands
        self.elseCommands = elseCommands
        pass

class CommandIfThen(Command):
    def __init__(self, line_number, condition, thenCommands):
        super().__init__(line_number=line_number)
        self.condition = condition
        self.thenCommands = thenCommands
        pass

class CommandWhileDo(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass

class CommandRepeatUntil(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass

class CommandForFromToDo(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass

class CommandForFromDowntoDo(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass


class CommandRead(Command):
    def __init__(self, line_number, identifier):
        super().__init__(line_number=line_number)
        self.identifier = identifier
        pass

    def generateCode(self, p):
        self.identifier.declaration.initialized = True
        instructions.READ(p, self.identifier)
        

class CommandWrite(Command):
    def __init__(self, line_number, value):
        super().__init__(line_number=line_number)
        self.value = value
        pass

    def generateCode(self, p):
        instructions.WRITE(p, self.value)