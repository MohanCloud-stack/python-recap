from collections import defaultdict
d={'a':10}
print(d['a'])
# print(d['wrong'])
# after adding the defaultdict
d=defaultdict(lambda:0)
d['correct']=100
print(d['correct'])
print(d['wrong'])
print(d)
