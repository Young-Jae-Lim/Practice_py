import random

a=[]
for i in range(20):
    x = random.randint(-300,300)
    a.append(x)
b=[]
for j in range(len(a)):
    for k in range(j,len(a)):
        for z in range(k,len(a)):
            b.append(sum([a[j], a[k], a[z]]))

b = sorted(b, key=abs)
print(b)
print(b[-1])