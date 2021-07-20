import sys
sys.stdin = open('BOJ16235.txt','r')
from pprint import pprint as pp


N,M,K = map(int,input().split())
land = [[5]*N for _ in range(N)]
nutrition = [[*map(int,input().split())] for _ in range(N)]
tree_info = [[*map(int,input().split())] for _ in range(M)]
tdict = dict()

for x,y,z in tree_info:
    if (x,y) not in tdict:
        tdict[(x,y)] = []
    tdict[(x,y)].append(z)
for k in tdict.keys():
    tdict[k].sort()
print(tdict)
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def isMap(x,y):
    return 0<=x<N and 0<=y <N


def solve(K):
    dead = {}
    for _ in range(K):
        # spring
        for (x,y) in tdict.keys():
            for i in range(len(tdict[(x,y)])):
                
                if tdict[(x,y)][i] <= land[x-1][y-1]:
                    land[x-1][y-1] -= tdict[(x,y)][i]
                    tdict[(x,y)][i] += 1
                else:
                    if (x,y) not in dead:
                        dead[(x,y)] = []
                    dead[(x,y)].extend(tdict[(x,y)][i:])
                    tdict[(x,y)] = tdict[(x,y)][:i]
                    
                    break 
        print(tdict)    
        empty_keys = [k for k in tdict.keys() if not tdict[k]]   
        for k in empty_keys:
            del tdict[k]

        # summer    
        for (x,y) in dead.keys():
            for j in dead[(x,y)]:
                land[x-1][y-1] += j//2
        
        # fall
        new_tree = [] 
        for (x,y) in tdict.keys():
            for tree in tdict[(x,y)]:
                if tree %5 == 0:
                    for d in range(8):
                        nx,ny = x+dx[d], y +dy[d]
                        if isMap(nx-1,ny-1):
                            new_tree.append((nx,ny))
        print(new_tree)
        for (x,y) in new_tree:
            if (x,y) not in tdict:
                tdict[(x,y)] = []
            tdict[(x,y)].append(1)
        
        for k in tdict.keys():
            tdict[k].sort()

        # winter 
        for x in range(N):
            for y in range(N):
                land[x-1][y-1] += nutrition[x-1][y-1]
    
    return len(tdict.keys())


# pp(land)
# pp(nutrition)
# pp(tree_info)

print(solve(K))