import sys
sys.stdin = open('BOJ10021.txt','r')

from collections import defaultdict,deque
from itertools import combinations as comb


N,C = map(int,input().split(' '))
graph = dict({'e':[],'v':[tuple(map(int,input().split(' '))) for _ in range(N)]})

def check_cost(xa,ya,xb,yb):
    return (xa-xb)**2 + (ya-yb)**2

for a,b in comb(graph['v'], 2):
    xa,ya = a
    xb,yb = b
    cost = check_cost(xa,ya,xb,yb) 
    if cost >= C:
        graph['e'].append((cost,a,b))
        graph['e'].append((cost,b,a))

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node]  = find(parent[node])
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    cost = 0
    for node in graph['v']:
        make_set(node)

    edges = graph['e']
    edges.sort()

    for edge in edges:
        weight,node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v,node_u)
            cost += weight
    return cost

# total = 0
# for cost,a,b in kruskal(graph):
#     total += cost
# print(total)
print(kruskal(graph))

# 최소신장트리, 크루스칼 알고리즘 인듯? 

#  ㅠㅠ 망했다 크루스칼 안됨 
#  간선 갯수가 매우 많아질 수 있으므로 프림 알고리즘 사용해야함 