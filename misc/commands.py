class Command:
    def __init__(self, line_number):
        self.line_number = line_number
        pass

    def generateCode(self):
        print(f"Generate Code not defined for {self.__class__}")

class CommandAssign(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass

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
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass

class CommandWrite(Command):
    def __init__(self, line_number):
        super().__init__(line_number=line_number)
        pass