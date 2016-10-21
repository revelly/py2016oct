#operator emulation
"""
__add__ +
__mul__ *
__sub__ -
__and__ &
__or__ |
__div__ /
__mod__ %
These are called magic method
Mod is unary
"""

class Car:
    def __init__(self, seats):
        self.seats = seats
    def __and__(self, other):
        return self.seats == other.seats


zen = Car(4)
swift = Car(4)
innova = Car(8)

print("About Zen And Innova")
if zen & innova:
    print("they are same")
else:
    print("they are not same")


print("About Zen And Swift")
if zen & swift:
    print("they are same")
else:
    print("they are not same")
