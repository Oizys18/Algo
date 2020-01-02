# 연결 요소의 개수
import collections
N, M = map(int, input().split())
edges = {}
for i in range(1,N+1):
    edges[i] = []

for j in range(M):
    u, v =  map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

visit = [0]*(N+1)
hi = 1
def BFS(node):
    global hi
    queue = collections.deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if not visit[node]:
            visit[node] = hi
            for n in edges[node]:
                if not visit[n]:
                    queue.append(n)
    hi += 1

for k in range(1,N+1):
    if not visit[k]:
        BFS(k)
print(len(set(visit))-1)
