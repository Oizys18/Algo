import sys
sys.stdin = open('BOJ16235.txt','r')
from pprint import pprint as pp


N,M,K = map(int,input().split())
land = [[5]*N for _ in range(N)]
nutrition = [[*map(int,input().split())] for _ in range(N)]
tree_info = [[*map(int,input().split())] for _ in range(M)]
tdict = dict()

for x,y,z in tree_info:
    tdict[(x,y)] = tdict.get((x,y),[])
    tdict[(x,y)].append(z)
print(tdict)
def solve(K):
    dead = []
    for _ in range(K):
        # spring
        for (x,y) in tdict.keys():
            for i in range(len(tdict[(x,y)])):
                if tdict[(x,y)][i] <= land[x][y]:
                    land[x][y] -= tdict[(x,y)][i]
                    tdict[(x,y)][i] += 1
                else:
                    dead.add((x,y,i))
        # summer
        # fall
        # winter 
    # pass
pp(land)
pp(nutrition)
pp(tree_info)
solve(K)