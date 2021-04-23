# 숫자게임
import itertools
N = int(input())
res = [0]*(N+1)
ndic = {}
for i in range(1,N+1):
    ndic[i] = [*map(int,input().split())]

for k in ndic.keys():
    ktemp = 0
    for p in itertools.combinations(ndic[k],3):
        temp = int(str(sum(p))[-1])
        if ktemp < temp:
            ktemp = temp
    res[k] = ktemp
mr = max(res)
for idx in range(N,0,-1):
    if res[idx] == mr:
        print(idx)
        break



"""
7
2 3 3 2 10
2 3 4 2 3
7 5 5 4 9
1 1 1 1 1
5 5 5 5 8 
3 3 2 4 5 
3 3 3 3 3 
"""