# def add(n1,n2):
#     print(n1+n2)

# number1=10
# number2=input("Enter the second number")
# add(number1,number2)
# try:
#     result=10+'10'
# except:
#     print("Hey it's look like you haven't added properly")
# else:
#     print("Add went Well")
#     print(result)
try:
    f=open("testfile",'r')
    f.write("write a test line")
except TypeError:
    print("There was a type error")
except :
    print("Hey You have an OS error")
finally:
    print("I will run No matter what!!!")
def askforint():
    while True:
        try:
            result=int(input("Please provide the number"))
        except:
            print("Whoops!!That not a number")
            continue
        else:
            print("Yes thank you!!")
            break
        finally:
            print("End Of try/except/finally")
            print("I will always run at end")
askforint()