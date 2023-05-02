lis=["1","2","3","4"]
if "0" not in lis:
    print("a")



        r2=list(i)
    r3=list(i)
    r2.remove("a")
    r2.remove("b")
    fre=0
    li=[]
    for va in ["1","2","3","4"]:
        p=r2.index(va)
        if p==int(va)-1:
            fre+=1
            li.append(va)
        for i2 in li:
            po=r3.index(i2)
            if po+1 != (r3.index("a") or r3.index("b")):
                if r3 not in l:
                    l.append(i)

    fre=0
    for va in ["1","2","3","4"]:
        p=r2.index(va)
        if p==int(va)-1:
            fre+=1