# DFS/BFS Silver 1
# DFS 미해결 ㅠ 
N, M, V = map(int, input().split())
edges = {}
for i in range(1, N+1):
    edges[i] = []

for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)
# print(edges)
for e in edges.keys():
    edges[e] = sorted(edges[e])

resBFS = []
visit = [0]*N
visit[0] = V

flag = 0
def DFS(s, k):
    global flag 
    if k == N:
        for i in visit:
            if i:
                print(i, end=' ')
        print()
        flag = 1
        return
    else:
        if flag:
            return
        for i in edges[s]:
            if i in visit:
                continue
            visit[k] = i
            DFS(i, k+1)
            visit[k] = 0


def BFS(start):
    visit = [0]*(N+1)
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if not visit[node]:
            visit[node] = 1
            resBFS.append(node)
            for i in edges[node]:
                queue.append(i)


DFS(V, 1)
BFS(V)

for k in resBFS:
    print(k, end=' ')
print()
