# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print("Invalid operands")

# try:
#     x=5
#     y=0
#     z=x/y
# except ZeroDivisionError:
#     print("Division By zero is not allowed")
# finally:
#     print("All done")
def ask():
    while True:
        try:
            num=int(input("enter the number"))
        except:
            print("Invalid Input")
            continue
        else:
            print(num*num)
            break
        finally:
            print("I will run ")
ask()
    


