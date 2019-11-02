# 구현
import sys
sys.stdin = open('input6.txt','r')


import collections



for T in range(int(input())):
    N, M = map(int,input().split())

    def BFS(node, goal):
        visit = [0]*1000001
        queue = collections.deque([(0,node)])
        while queue:
            depth, node = queue.popleft() 
            # print(depth, node)
            if node > 1000000:
                continue
            else:
                if visit[node]:
                    continue
                else:
                    visit[node] = node
                    if node * 2 == goal:
                        return depth + 1
                    else:
                        queue.append((depth+1, node*2))
                    if node + 1 == goal:
                        return depth + 1
                    else:
                        queue.append((depth+1, node+1))
                    if node - 10 == goal:
                        return depth + 1
                    else:
                        queue.append((depth+1, node-10))
                    
                    if node - 1 == goal:
                        return depth + 1
                    else:
                        queue.append((depth+1, node-1))
                    
    print(f"#{T+1} {BFS(N,M)}")
