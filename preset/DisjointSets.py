def MakeSet(x):
    p[x] = x

def FindSet(x):
    if x == p[x]:
        return x
    else:
        return FindSet(p[x])
def Union(x, y):
    p[FindSet(y)] = FindSet(x)

N = 8
p = [0]*(N+1)
for i in range(N+1):
    MakeSet(i)
line = [(1,3),(2,5),(3,4),(1,4),(2,7)]
for x,y in line:
    Union(x,y)
print(p)