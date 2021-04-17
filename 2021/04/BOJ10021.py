import sys
sys.stdin = open('BOJ10021.txt','r')

from itertools import combinations as comb
from collections import defaultdict
from heapq import *  

# 가중치 계산 
def check_cost(node1,node2):
    return (node1[0]-node2[0])**2 + (node1[1]-node2[1])**2

# 프림 알고리즘 
def prim(start_node, edges):
    cost = 0
    # mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight,n1,n2))
        adjacent_edges[n2].append((weight,n2,n1))

    connected_nodes = [0]*(N+1)
    connected_nodes[start_node] = 1
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if not connected_nodes[n2]:
            connected_nodes[n2]= 1
            # mst.append((weight,n1,n2))
            cost += weight
            for edge in adjacent_edges[n2]:
                if  not connected_nodes[edge[2]]:
                    heappush(candidate_edge_list,edge)
    # return mst 
    return cost


# 데이터 입력 
N,C = map(int,input().split(' '))

# node 만들기 
# data = dict({i:tuple(map(int,input().split())) for i in range(N)})
edges = []
data = {}
for i in range(N):
    a,b = map(int,input().split())
    for node in data.keys():
        cost = check_cost(data[node],(a,b))
        if cost >= C:
            edges.append((cost,node,i))
    data[i] = (a,b)
        
print(edges)
print(data)

# # # 간선 만들기 (거리비용 C이상)
# for node1,node2 in comb(data, 2):
#     cost = check_cost(data[node1],data[node2]) 
#     if cost >= C:
#         edges.append((cost,node1,node2))


# print(prim(0,edges))



"""
프림 알고리즘으로 해도 메모리초과...
"""











""" 최초 제출 코드 
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
print(kruskal(graph))
"""
# 최소신장트리, 크루스칼 알고리즘 인듯? 

#  ㅠㅠ 망했다 크루스칼 안됨 
#  간선 갯수가 매우 많아질 수 있으므로 프림 알고리즘 사용해야함 