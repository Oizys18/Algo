import sys
sys.stdin=open('input.txt','r')
from pprint import pprint as pp
import itertools

for T in range(int(input())):
    N, M, C = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mineral = []
    for x in range(N):
        for y in range(M):
            if mat[x][y] == 1:
                robot = (x,y)
            if mat[x][y] > 1:
                mineral.append((x,y))
    moveCost = {}
    cntMineral = len(mineral)
    for m in range(cntMineral):
        a,b = mineral[m]
        cost = (abs(robot[0]-a) + abs(robot[1]-b)) * 2
        moveCost[m] = (cost,mat[a][b])
    print(moveCost)
    print()

def perm(node):
    stack = []
    visit = [0] * cntMineral
    stack.append(node)
    while stack:
        node = stack.pop(0)
        if not visit[node]:
            visit[node] = 1
            mineRange =
            for i in range(0:cntMineral,cntMineral:)


totalE = 0
res = []
for a in range(cntMineral):
    visit = [0] * cntMineral
    if totalE + moveCost[a][0] <= C and not visit[a]:
        totalE += moveCost[a][0]
        visit[a] = 1


    for b in range(5):
        if totalE + moveCost[b][0] <= C and not visit[b]:
            totalE += moveCost[b][0]
            visit[b] = 1
        for c in range(5):
            if totalE + moveCost[c][0] <= C and not visit[c]:
                totalE += moveCost[c][0]
                visit[c] = 1
            for d in range(5):
                if totalE + moveCost[d][0] <= C and not visit[d]:
                    totalE += moveCost[d][0]
                    visit[d] = 1
                for e in range(5):
                    if totalE + moveCost[e][0] <= C and not visit[e]:
                        totalE += moveCost[e][0]
                        visit[e] = 1

    totalE = 0
    res.append(visit)

print(res)

#
# a = [1,2,3,4,5]
# print(a[:3-1],a[3:])