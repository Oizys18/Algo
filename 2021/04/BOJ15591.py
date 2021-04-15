#BOJ 15591
import sys
sys.stdin = open('BOJ15591.txt', 'r')
from pprint import pprint as pp 

N,Q = map(int, input().split(' '))
mat = [[0]*(N+1) for _ in range(N+1)]
graph = {i:[] for i in range(N+1)}

for _ in range(N-1):
    p,q,r = map(int,input().split(' '))
    mat[p][q] = r
    mat[q][p] = r
    graph[p].append(q)
    graph[q].append(p)
print(graph)

def checkU(start,now,end,usado=[],visit=[0]*(N+1),cnt=0):
    visit[now] = 1
    print(now,cnt,visit)
    if now == end:
        mat[start][end] = min(usado)
        mat[end][start] = min(usado)
        print(min(usado))
        return
    nxt_path = graph[now]
    for edge in nxt_path:
        if not visit[edge]:
            visit[edge] = 1
            usado.append(mat[now][edge])
            checkU(start,edge,end,usado,visit,cnt+1)
            usado.pop()
            visit[edge] = 0

for e in range(1,N+1):
    for f in range(e,N+1):
        if e!=f: 
            print('---------------',e,f)
            checkU(e,e,f)
            pp(mat)
checkU(3,3,4)
pp(mat)

# for _ in range(Q):
#     k,v = map(int,input().split(' '))
#     temp_usado = []
#     for e in range(1,N+1):
#         if e == v:
#             continue
#         checkU(v,v,e)

