# BJ2606 바이러스 
import sys
sys.stdin = open('input3.txt','r')


def BFS(node):
    queue = []
    visit = [0]*(T+1)
    queue.append(node)
    while queue:
        node = queue.pop(0)
        if not visit[node]:
            visit[node] = 1
            if node in connect.keys():
                for v in connect[node]:
                    if not visit[v]:    
                        queue.append(v)
    result = sum(visit)
    if result == 1:
        return 0 
    else:
        return result - 1


T = int(input())
connect = {}
for i in range(int(input())):
    x,y = map(int,input().split())
    if x not in connect.keys():
        connect[x] = []
    if y not in connect.keys():
        connect[y] = []
    connect[y].append(x)    
    connect[x].append(y)
print(BFS(1))


    