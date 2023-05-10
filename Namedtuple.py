from collections import namedtuple
Dog=namedtuple('Dog',['age','breed','name'])
print(type(Dog))
sammy=Dog(age=5,breed='Husky',name='Sam')
print(type(sammy))
print(sammy.age)
print(sammy[1])