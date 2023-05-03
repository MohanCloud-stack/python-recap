class Dog():
    #it is not connected to any self so
    # it is a class object Attribute
    species="mamal"
    def __init__(self,breed,name,spot):
        self.breed=breed
        self.name=name
        self.spot=spot
    # Operations/ actions
    def bark(self,number):
        print("WOOF! My name is {} and number is {}".format(self.name,number))

m1=Dog(breed="lab",name="jimmy",spot=True)
m1.bark(32)