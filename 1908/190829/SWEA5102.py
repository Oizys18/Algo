# SWEA 5102

"""

"""

import sys
sys.stdin = open('input5.txt','r')
def BFS(depth,start,end):
    queue = []
    visit = []
    queue.append((depth,start))
    while queue:
        depth, node = queue.pop(0)
        if node == end:
            # print(visit)
            return depth
        if node not in visit:
            visit.append(node)
            if node in graph.keys():
                for n in graph[node]:
                    if (depth+1,n) not in queue:
                        queue.append((depth+1,n))
    return 0
    
for T in range(int(input())):
    V, E = map(int,input().split())
    graph = {}
    for _ in range(E):
        A,B = map(int,input().split())
        if A not in graph.keys():
            graph[A] = []
        graph[A].append(B)
        if B not in graph.keys():
            graph[B] = []
        graph[B].append(A)
    S, G = map(int,input().split())
    print("#{0} {1}".format(T+1, BFS(0,S,G))) 