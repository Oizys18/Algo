# 숫자게임
import itertools

N = int(input())
res = [0]*10
ndic = {}
for i in range(1,N+1):
    ndic[i] = [*map(int,input().split())]

for k in ndic.keys():
    ktemp = 0
    for p in itertools.permutations(ndic[k],3):
        temp = int(str(sum(p))[-1])
        if ktemp < temp:
            ktemp = temp
    if res[ktemp]:
        if res[ktemp] < k:
            res[ktemp] = k
        else:
            continue
    else:
        res[ktemp] = k    

for r in range(9,0,-1):
    if r:
        print(res[r])
        break

"""
2
7 5 5 4 9
2 3 3 2 10
""" 