from enum import Enum

class REG(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'
    H = 'h'

    def __str__(self):
        return self.value