import sys
sys.stdin = open('BOJ1197.txt','r')
from collections import defaultdict
from heapq import *  
"""
최소신장트리 문제, 
기본기 
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
"""

V,E = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(E)]
"""graph
v1, v2, weight
"""
def my_prim(start,edges):
    mst = list()
    # 인접 정점 정보 저장
    adj_edges = defaultdict(list)
    for n1,n2,w in edges:
        adj_edges[n1].append((w,n1,n2))
        adj_edges[n2].append((w,n2,n1))
    
    # 시작 정점 추가 
    connected = [0]*(V+1)
    connected[start] = 1
    
    # 후보 정점들 초기화
    candidate = adj_edges[start]
    print(candidate,'can')
    heapify(candidate)
    while candidate:
        w,n1,n2 = heappop(candidate)
        if not connected[n2]:
            connected[n2] = 1
            mst.append((w,n1,n2))

            for edge in adj_edges[n2]:
                if not connected[edge[2]]:
                    heappush(candidate,edge)
    return mst 

# # 프림 알고리즘
# def prim(start_node, edges):
#     cost = 0
#     # mst = list()
#     adjacent_edges = defaultdict(list)
#     for n1, n2, weight in edges:
#         adjacent_edges[n1].append((weight,n1,n2))
#         adjacent_edges[n2].append((weight,n2,n1))

#     connected_nodes = [0]*(V+1)
#     connected_nodes[start_node] = 1
#     candidate_edge_list = adjacent_edges[start_node]
#     heapify(candidate_edge_list)

#     while candidate_edge_list:
#         weight, n1, n2 = heappop(candidate_edge_list)
#         if not connected_nodes[n2]:
#             connected_nodes[n2]= 1
#             # mst.append((weight,n1,n2))
#             cost += weight

#             for edge in adjacent_edges[n2]:
#                 if  not connected_nodes[edge[2]]:
#                     heappush(candidate_edge_list,edge)
#     return cost
print(my_prim(1,graph))