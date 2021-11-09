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
p = [0]*N
for i in range(N):
    MakeSet(i)
line = [(1, 3), (2, 5), (3, 4), (1, 4), (2, 7)]
for x, y in line:
    Union(x, y)
print(p)
