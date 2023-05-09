def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)
g=simple_gen()
print(g)
for strings
str="hello"
s_iter=iter(str)
print(next(s_iter))
# for num in str:
#     print(num)