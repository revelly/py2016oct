class Man:
    def getIntelligence(self):
        print("High intelligence")
    def getFairness(self):
        print("Low")
class Woman:
    def getIntelligence(self):
        print("Low intelligence")
    def getFairness(self):
        print("High")

class Kid(Man, Woman):
    def getFairness(self):
        print("High")


lilly = Kid()
lilly.getIntelligence()
lilly.getFairness()
