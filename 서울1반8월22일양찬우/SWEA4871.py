# SWEA 4871

import sys
sys.stdin = open('input.txt','r')

def dfs(graph, start_node):
    visit = []
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

for T in range(int(input())):
    V, E = map(int,input().split())
    # mat = [[0 for _ in range(V+1)] for _ in range(V+ 1)]
    ndict = {}
    for i in range(1,V+1):
        ndict[i] = []
    for _ in range(E):
        a, b = map(int,input().split())
        ndict[a].append(b)

        # mat[a][b] = 1
    S,G = map(int,input().split())
    path = dfs(ndict,S)

    print("#{0}".format(T+1),end=' ')  
    if S in path and G in path:
        print(1)
    else:
        print(0)




