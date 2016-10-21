class Animal2:
    def __init__(self,breed):
        self.breed=breed
    def getbreed(self):
        print("Print from parent class Animal2")
        return self.breed
    
class Animal:
    def __init__(self,breed):
        self.breed=breed
    def getbreed(self):
        print("Print from parent class")
        return self.breed
    def getbreed2(self):
        print("Print from parent class brees2")
        return self.breed
    
class Dog(Animal2, Animal):
    def spreak(self):
        print("bouh.. bouh..")
    def getbreed(self):
        #fd =super.getbreed()
        print("I m a ",self.breed)
    def getparentbreed(self):
        print(super(Dog, self).getbreed2())

        
tommy = Dog("Lab")
print(tommy.getbreed())
tommy.spreak()
tommy.getparentbreed()
        
