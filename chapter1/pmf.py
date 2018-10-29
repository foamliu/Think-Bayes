from chapter1.thinkbayes import Pmf

pmf = Pmf()
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1 / 6.0)

print(pmf)
