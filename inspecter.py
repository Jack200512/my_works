msg=input("msg:")
rsl=input("rsl:")
t_m=msg.title()
t_r=rsl.title()
a=t_m.split()
lst=[]
for i in a:
    nub=t_r.find(i)
    if nub != -1:
        lst.append(1)
    else:pass
print(len(lst)/len(a))