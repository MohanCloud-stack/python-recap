import os
import shutil
import send2trash
try:
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir('C:\\Users'))
    # f=open('demo.txt','w+')
    # f.write("this is a test string")
    # f.close()
    # print(shutil.move('C:\\Users\\MOHAN\\PycharmProjects\\demo.txt',os.getcwd()))
    print(send2trash.send2trash('demo.txt'))
    print(os.listdir())
except FileNotFoundError:
    print("The file might be missing ")
finally:
    print("I have completed the program")
file_path="C:\\Users\\MOHAN\\PycharmProjects\\awsproject\\python-recap"
for folder in os.walk(file_path):
    print(f"Currently Looking at {folder}")
    print("\n")