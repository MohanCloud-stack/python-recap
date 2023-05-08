class Animal():
    def __init__(self):
        print("Animal Created")
    def eat(self):
        print("I am eating")
    def whoami(self):
        print("I am an Animal")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("this is Dog")
    def eat(self):
        print("I am Dog and I am eating")
    def whoami(self):
        print("I am Dog")
d1=Dog()
d1.eat()
d1.whoami()