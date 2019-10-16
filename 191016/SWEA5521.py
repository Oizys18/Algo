import sys
sys.stdin = open('input5.txt','r')

for T in range(int(input())):
    N,M = map(int,input().split())
    edges={}
    for i in range(1,N+1):
        edges[i] = []
    for _ in range(M):
        a,b = map(int,input().split())
        edges[a].append(b)
        edges[b].append(a)
        
    visit = [0]*(N+1)
    def BFS(depth, node):
        global visit
        queue = []
        queue.append((depth, node))
        while queue:
            depth, node = queue.pop(0)
            if depth > 2:
                break
            if not visit[node]:
                visit[node] = 1
                for i in edges[node]:
                    queue.append((depth+1, i))
        return sum(visit)-1
    
    print(f"#{T+1} {BFS(0,1)}")

    