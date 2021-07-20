import sys
sys.stdin = open('BOJ16235.txt','r')
from pprint import pprint as pp
from collections import deque

N,M,K = map(int,input().split())
land = [[5]*N for _ in range(N)]
nutrition = [[*map(int,input().split())] for _ in range(N)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

tdict = dict()
for _ in range(M):
    x,y,z = map(int,input().split())
    if (x,y) not in tdict:
        tdict[(x,y)] = deque()
    tdict[(x,y)].append(z)


def isMap(x,y):
    return 0<=x<N and 0<=y <N

for _ in range(K):
    dead = {}
    new_tree = deque()
    for (x,y) in tdict.keys():
        for i in range(len(tdict[(x,y)])-1,-1,-1):
            if tdict[(x,y)][i] <= land[x-1][y-1]:
                land[x-1][y-1] -= tdict[(x,y)][i]
                tdict[(x,y)][i] += 1
                if tdict[(x,y)][i]%5 == 0:
                    for d in range(8):
                        nx,ny = x+dx[d], y +dy[d]
                        if isMap(nx-1,ny-1):
                            new_tree.append((nx,ny))
            else:
                if (x,y) not in dead:
                    dead[(x,y)] = deque()
                dead[(x,y)].append(tdict[(x,y)][i])
                
                dead[(x,y)].extend(tdict[(x,y)][i:])
                tdict[(x,y)] = tdict[(x,y)][:i]
                break 

    empty_keys = [k for k in tdict.keys() if not tdict[k]]   
    for k in empty_keys:
        del tdict[k]

    for (x,y) in dead.keys():
        for j in dead[(x,y)]:
            land[x-1][y-1] += j//2
    
    for (x,y) in new_tree:
        if (x,y) not in tdict:
            tdict[(x,y)] = deque()
        tdict[(x,y)].append(1)

    for x in range(N):
        for y in range(N):
            land[x-1][y-1] += nutrition[x-1][y-1]
    pp(tdict)
total = 0
for k in tdict.values():
    total += len(k)

print(total)