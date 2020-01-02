import sys
sys.stdin = open('input.txt','r')
line = list(map(int,input().split()))
mat = [[0]*8 for _ in range(8)]
for i in range(0,len(line),2):
    mat[line[i]][line[i+1]] = line[i+1]

# DFS와 동일하지만 queue를 사용해 앞에서부터 뺀다면 BFS 구현 가능  
def BFS(G,v):
    visited = [0]*8
    visited[0] = True
    queue = []
    queue.append(v)
    visit = []
    
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit.append(t) 
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
    return visit

print(BFS(mat,1))





