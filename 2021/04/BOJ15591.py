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

"""
아주 오랫동안 풀지 못했다....
1. 처음엔 recursive 에러가 발생했다. 너무 깊이 들어간 듯 
2. queue와 while을 사용하자 에러는 발생하지 않았지만 시간초과가 발생했다. 
  문제는 처음 그래프 데이터를 받는 부분에서 N*N 행렬을 만든 것이 잘못이었다. 
  dictionary 로 수정하고 deque를 사용해서 풀었다. 
3. 문제 자체의 아이디어 측면에서 만약 K보다 크다면 해당 노드는 방문하지 않아도 된다는 점을 먼저 파악했어야 했다. 
   처음 풀 땐 아예 BFS를 돌고 행렬에 전부 값을 저장한 후 min()으로 답만 프린트할 생각이었는데, 아주 아주 잘못된 생각이었다. 
   시간 복잡도와 공간 복잡도 계산하는 연습을 해야겠다 
"""