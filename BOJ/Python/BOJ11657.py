from pprint import pprint as pp
import sys
sys.stdin= open('BOJ11657.txt','r')
# 타임머신

from collections import defaultdict
N,M = map(int,sys.stdin.readline().split())
mat = [[*map(int,sys.stdin.readline().split())] for _ in range(M)]
line = defaultdict(list)

# 시작은 1번 도시
for A,B,C in mat:
    line[A].append((C,B))
    line[B].append((C,B))
pp(line)

"""
벨만포드, 최단거리 알고리즘 중에 음수값이 있어도 상관없는 알고리즘. 

벨만-포드 알고리즘(Bellman-Ford Algorithm)
최단 거리를 찾는 알고리즘
시간복잡도 O(VE) V: 정점 수, E: 간선 수
방향 그래프에서 음의 가중치를 지닌 간선이 존재할 때 사용
음의 순환이 있는 경우에는 최단 거리를 찾지 못함

작동 원리
시작 노드에 대해서 거리를 0으로 초기화, 나머지 노드는 거리를 무한으로 설정
정점 수(n) -1 만큼 다음 과정을 반복
매 반복 마다 모든 간선 확인
현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
n-1번 반복 이후, n번째 반복에서도 거리 값이 갱신된다면 음수 순환이 존재
다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것입니다. 
다익스트라는 방문하지 않는 노드 중에서 최단 거리가 가장 가까운 노드만을 방문했습니다.
"""