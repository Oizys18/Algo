#BOJ 15591
import sys
sys.stdin = open('BOJ15591.txt', 'r')
from pprint import pprint as pp 


from collections import deque, defaultdict

N,Q = map(int, input().split(' '))
graph = defaultdict(list)

for p,q,r in [map(int,input().split(' ')) for _ in range(N-1)]:
    graph[p].append((q,r))
    graph[q].append((p,r))

def solve(k,v,visit):
    cnt = 0
    queue = deque()
    queue.appendleft(v)
    while queue:
        edge = queue.popleft()
        visit[edge] = 1
        for edge,length in graph[edge]:
            if length >= k and not visit[edge]:
                visit[edge] = 1
                cnt += 1
                queue.appendleft(edge)
    return cnt

for k,v in [map(int,input().split(' ')) for _ in range(Q)]:
    print(solve(k,v,[0]*(N+1)))

