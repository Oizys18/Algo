# 최소 신장 트리 : 프림 or 크루스칼 
"""
!!!! 노드의 수가 작은데 간선의 수가 많은 경우(밀집 그래프 경우)>>> 
노드 기준으로 찾는 프림 알고리즘이 유리함

!!!! 간선의 수가 작은 경우 >>> 
간선을 기준으로 선택하는 크루스칼이 유리함
"""
"""
<최소 신장 트리 찾기 - 프림 알고리즘>
# 한 정점에 연결된 간선들 중 하나씩 선택하면서 최소 신장 트리를 만들어 가는 방식

# 프림 알고리즘의 동작
1. 임의의 정점을 하나 선택해서 시작
2. 선택한 정점들과 인접하는 정점들 중에 최소 비용의 간선이 존재하는 정점 선택
    (무한대로 해놓고 채워넣으면서 인접 여부 파악함)
3. 모든 정점이 선택될 때까지 두 번째 과정 반복

>> 정점의 수 n개, 시작 정점을 제외한 n-1개의 정점 선택
>> n-1개의 간선 선택됨
>> 선택된 정점들과 간선들은 하나의 트리 구성

# 프림 알고리즘이 동작하려면 두 종류의 상호 배타 집합들 정보가 필요함
- 트리 정점들(Tree vertices): 최소 신장 트리를 만들기 위해 선택된 정점들
- 비트리 정점들(Non-tree vertices): 선택되지 않은 정점들
"""


# 변수  
INF = 50000
# 정점 갯수
N = 5
# 그래프
G = [
    [(1,2),(4,3),(3,2)],[(1,2),(4,3),(3,2)],[(1,2),(4,3),(3,2)],[(1,2),(4,3),(3,2)],[(1,2),(4,3),(3,2)]
]


def MST_PRIM(G, s):  # G: 그래프, s: 시작 정점
    key = [INF] * N  # 가중치를 무한대로 초기화
    pi = [None] * N  # 트리에서 연결될 부모 정점 초기화
    visited = [False] * N  # 방문여부 초기화
    key[s] = 0  # 시작 정점의 가중치를 0으로 설정

    for _ in range(N):  # 정점의 개수만큼 반복
        minIndex = -1
        mini = INF
        for i in range(N):  # 방문 안한 정점중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < mini:
                mini = key[i]
                minIndex = i
        visited[minIndex] = True  # 최소 가중치 정점 방문처리
        for v, val in G[minIndex]:  # 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]:
                key[v] = val  # 가중치 갱신
            pi[v] = minIndex  # 트리에서 연결될 부모 정점

    return pi
    
print(MST_PRIM(G,0))



"""
<최소 신장 트리 찾기 - 크루스칼 알고리즘>
# 최소 가중치 간선을 하나씩 선택해서 최소 신장 트리를 찾는 알고리즘
# Disjoing-set을 이용한다. 
# N개의 정점을 포함하는 그래프에서 n-1개의 간선을 선택하는 방식
# 프림이 트리를 확장시켜가는 방식이라면,
# 크루스칼은 간선을 선택해 나가는 과정에 여러 개의 트리들이 존재한다.

- 초기 상태는 n개의 정점들이 각각 하나의 트리가 됨
    >> 하나의 정점을 포함하는 n개의 상호 배타 집합 존재
- 간선을 선택하면 간선의 두 정점이 속한 트리가 연결되고 하나의 집합으로 합쳐짐
- 사이클이 생기는 경우 제외시킴
    (선택한 간선의 두 정점이 이미 연결된 트리에 속한 정점들일 경우 사이클이 생김)
    >> 두 정점에 대해 같은 집합의 원소 여부 검사해야 함

# 크루스칼 알고리즘의 동작
1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리 증가시킴
3. 사이클이 존재하면 다음으로 가중치가 낮은 간선을 선택한다.
4. n-1개의 간선이 선택될 때까지 두 번째 과정을 반복한다.
"""

#변수
G = []
parent = {}
rank = {}


def MakeSet(x):
    parent[x] = x
    rank[x] = 0

def FindSet(x):
    if x != parent[x]:
        parent[x] = FindSet(parent[x])
    return parent[x]

def Union(x, y):
    rootX = FindSet(x)
    rootY = FindSet(y)

def MST_KRUSKAL(G):
    mst = [] # 공집합
    for i in range(N):
        MakeSet(i) # 각각 원소 1개를 갖는 상호배타 집합 생성

    G.sort(key = lambda t: t[2]) # 가중치 기준으로 정렬

    mst_cost = 0 # MST 가중치

    while len(mst) < N-1:
        u, v, val = G.pop(0) # 최소 가중치 간선 가져오기
        if FindSet(u) != FindSet(v): # 사이클이 생기지 않는 경우만 찾는다(같은 집합이 아닌지 확인)
            Union(u, v)
            mst.append((u, v)) # 트리에 (u, v) 추가가
            mst_cost += val

# MST_KRUSKAL(G)