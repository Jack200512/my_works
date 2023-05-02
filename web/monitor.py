"""四个班的班长和两个宿管查寝，有四个宿舍，每个宿舍都要有一个班长，
   若班长去自己班，则需要宿管陪同，宿管不去同一个宿舍，问有多少种方式"""

import itertools

re = list(itertools.permutations(["1", "2", "3", "4", "a", "b"], 6))
l = []
l2 = []
l3 = []


def f():
    for q in l:

        if q in re:
            re.remove(q)
    l.clear()


for i in re:
    r2 = list(i)
    strr = "".join(r2)
    for v in ["ab", "ba"]:
        a = strr.find(v)
        if a != -1:
            l.append(i)
f()
for i in re:
    r2 = list(i)
    strr = "".join(r2)
    ar = strr.find("a")
    br = strr.find("b")
    if ar == 0 or br == 0:
        l.append(i)
f()
for i in re:
    r2 = list(i)
    r2.remove("a")
    r2.remove("b")
    fre = 0
    for va in ["1", "2", "3", "4"]:
        p = r2.index(va)
        if p == int(va) - 1:
            fre += 1
    if fre >= 3:
        l.append(i)
f()
for i in re:
    r2 = list(i)
    r3 = list(i)
    r2.remove("a")
    r2.remove("b")
    for va in ["1", "2", "3", "4"]:
        p = r2.index(va)
        if p == int(va) - 1:
            strr = "".join(r3)
            ea = strr.find(va + "a")
            eb = strr.find(va + "b")
            if ea == -1 and eb == -1:
                if i not in l:
                    l.append(i)
f()
print(len(re))