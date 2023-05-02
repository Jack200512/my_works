"""某电视台播放6个广告,其中3个是商业广告,2个是宣传广告,1个是公益广告。
   要求最后播放的不能是商业广告,2个宣传广告不能连续播放,宣传广告与商业广告
   也不能连续播放，则不同的播放方法有多少种？
"""
import itertools
ad = ["a", "b", "c", "d", "e", "f"]
rslt = list(itertools.permutations(ad, 6))
lst = []
lst2 = []
def f(x):
    for r in rslt:
        if r[5] == x:
            lst.append(r)
f("a")
f("b")
f("c")
for i in lst:
    rslt.remove(i)
for r2 in rslt:
    l2 = []
    vlu = ["de", "ed", "df", "fd", "ef", "fe"]
    strr = "".join(r2)
    for v in vlu:
        va = strr.find(v)
        l2.append(va)
    if sum(l2) == -6:
        lst2.append(r2)
print(len(lst2))