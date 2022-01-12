from Memory import manager
class Program:
    def __init__(self, variables, commands):
        self.variables = variables
        self.commands = commands
        # print('VARIABLES')
        # print(self.variables)
        # print('COMMANDS')
        # print(self.commands)

        #Program info
        self.instructions = []
        self.counter = 0

        #Init pamieci
        manager.checkMemory(self.variables)
        manager.assignMemToVariables()


        #Kompilacja
        self.translateCommands()

        print(self.commandsToText())

    def makeInstr(self, instrStr):
        self.incCounter()
        self.instructions.append(instrStr)

    def getCounter(self):
        return self.counter
    
    def incCounter(self):
        self.counter += 1

    def addFutureInstr(self, future):
        self.incCounter()
        self.instructions.append(future)
        return self.counter - 1

    def translateCommands(self):
        self.makeInstr("RESET a")
        self.makeInstr("RESET b")
        self.makeInstr("RESET c")
        self.makeInstr("RESET d")
        self.makeInstr("RESET e")
        self.makeInstr("RESET f")
        self.makeInstr("RESET g")
        self.makeInstr("RESET h")
        self.makeInstr("INC h")
        self.makeInstr("")
        for command in self.commands:
            command.generateCode(self)
            self.makeInstr("")

    def commandsToText(self):
        text = ""
        for instr,index in enumerate(self.instructions):
            text += f"{index}: {instr}\n"
        
        text = '\n'.join(self.instructions)
        text += "\nHALT"
        
        return text