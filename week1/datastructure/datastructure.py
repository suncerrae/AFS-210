from enum import Enum


class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for a in Countries:
    print(a.name + ' = '+ str(a.value))