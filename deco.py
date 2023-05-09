def hello(name="Jose"):
    #scope of below hello as well as welcome is within hello function
    print("The hello() function has been executed!!")
    def greet():
        return "\t This is a greet() func inside hello"
    def welcome():
        return "\t This is welcome() inside hello"
    if name == 'Jose':
        return greet
    else:
        return welcome 
mynewfunc=hello("Jose")
print(mynewfunc())
