def create_cubes(n):
    for x in range(n):
        yield x**3
for  i in create_cubes(10):
    print(i)
#fibonacci sequence
def gen_fib(n):
    a=1
    b=1
    for i in range(n):
       yield a 
       a,b=b,a+b
for i in gen_fib(10):
    print(i)