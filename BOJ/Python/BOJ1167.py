import sys
sys.stdin=open('BOJ1167.txt','r')
from pprint import pprint as pp
from collections import defaultdict
"""
트리가 입력으로 주어진다. 
먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 
정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고,
 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 
하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 
정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 
주어지는 거리는 모두 10,000 이하의 자연수이다.

트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 
트리의 지름을 구하는 프로그램을 작성하시오.
"""

V = int(input())
edges = defaultdict(list)

for v in range(V):
    node, *data, end = map(int,input().split())
    for i in range(0,len(data),2):
        edges[node].append((data[i],data[i+1]))
far = 0
deep = 0 
def dfs(node,total):
    global far
    global deep
    if far < total:
        far = total
        deep = node

    visit[node] = 1 
    for v,w in edges[node]:
        if not visit[v]:
            visit[v] = 1 
            dfs(v,total+w)
            visit[v] = 0
    visit[node] = 0
    return 



visit = [0]*(V+1)
visit[1] = 1
dfs(1,0)

dfs(deep,0)
print(far)


"""
지름을 구할 때, 모든 노드에 대해 for i in range(V):dfs(i) 해버리면 시간초과가 난다. 
아예 하나의 노드에 대해 제일 깊은 정점 하나를 구하고, 
그 정점에 대해 다시 dfs를 돌리면 제일 긴 트리를 구할 수 있다. 
"""

