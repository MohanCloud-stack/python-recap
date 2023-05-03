class Circle():
    #Class Object Attribute
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area=radius*radius*self.PI

    def getcircumference(self):
        return self.radius * self.PI * 2


c1 = Circle(32)
print(c1.PI)
print(c1.getcircumference())
print(c1.area)
