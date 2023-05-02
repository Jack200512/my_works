import itertools 
b=list(itertools.permutations(range(1,101), 3))
l=[]
for i in b:
    t=list(i)
    if 2*t[1]==(t[0]+t[2]):
        l.append(i)
print(len(l))