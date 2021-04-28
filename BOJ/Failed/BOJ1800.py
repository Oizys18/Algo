# BOJ1800 인터넷 설치 
import sys
sys.stdin = open('BOJ1800.txt','r')
from pprint import pprint as pp
from time import time
from collections import deque,defaultdict

start = time()

# N,P,K = map(int,input().split())
# edges = {i:[] for i in range(N+1)}
# mat = [list(map(int,input().split())) for _ in range(P)]

# for p in range(P):
#     A,B,price = mat[p]
#     edges[A].append((A,B,price))
#     edges[B].append((B,A,price))
# print('edges')
# pp(edges)

# print()
# print('----------')
# print('mat')
# pp(mat)
# print()


# visit = [0]*(N+1)
# visit[1] = 1
# ans = 1000000
# def DFS(now,visit,cnt):
#     global ans
#     if now == N:
#         print(visit)
#         ans = min(ans, sorted(visit)[-2])
#         return
#     if cnt == P: 
#         return 
    
#     for a,b,price in edges[now]:
#         if not visit[b]:
#             visit[b] = price
#             DFS(b,visit,cnt+1)
#             visit[b] = 0

# DFS(1,visit,0)

# print()
# print('----------') 
# print() 

# if ans == 1000000:
#     print(-1)
# else:
#     print(ans)

import heapq
import sys


INF = 1e15

def dijkstra(start, limit):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))  # (가중치, 인덱스)
    distance[start] = 0

    while q:
        cost, index = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[index] < cost:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인하면서 거리 업데이트
        for i in graph[index]:
            if i[0] > limit:
                if cost + 1 < distance[i[1]]:
                    distance[i[1]] = cost + 1
                    heapq.heappush(q, (cost + 1, i[1]))
            else:
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

    # limit 보다 큰 가격 k개 이상이면 False
    if distance[n] > k:
        return False
    else:
        return True


if __name__ == "__main__":
    n, p, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(p):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    left, right = 0, 1000001
    answer = INF
    while left <= right:
        mid = (left + right) // 2
        flag = dijkstra(1, mid)
        if flag:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    if answer == INF:
        print(-1)
    else:
        print(answer)
print(time()-start)

"""
# 시간초과 발생 
시간제한 : 2초 
메모리 : 512mb 

현재 알고리즘 : 재귀 
-> 인터넷 설명 
모든 재귀 호출에 대해 재귀 하수는 인수, 반환 주소, 지역 변수를 메모리의 스택에 할당합니다. 
이러한 데이터를 스택에 넣고(push) 꺼내는(pop) 데에는 시간이 소비됩니다. 
재귀 알고리즘은 최소 O(n)의 공간을 사용합니다. 여기서 n은 재귀 호출의 깊이(depth)입니다.
재귀는 계산이 중복되거나 하위 문제가 겹치는경우 비용이 많이 듭니다. 
어떤 경우에는 스택 오버플로가 발생할 수도 있습니다. 
이러한 이유로 하위 문제가 겹치는 경우에는 반복문을 사용하는 것(iterative)이 더 좋은 방법이 될 수 있습니다.





"""
