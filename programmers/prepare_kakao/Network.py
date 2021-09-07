from collections import defaultdict
def solution(n, computers):
    answer = 0
    edges = defaultdict()
    for idx,computer in enumerate(computers):
        edges[idx] = computer
    gvisit = [0]*n

    def bfs(start):
        q = [start]
        visit = [0]*n
        visit[start] = 1 
        while q:
            edge = q.pop(0)
            visit[edge] = 1 
            for idx,node in enumerate(edges[edge]):
                if node and not visit[idx]:
                    q.append(idx)
        return visit

    while sum(gvisit)!=n:
        nxt = 0
        for i in range(n):
            if not gvisit[i]:
                nxt = i
                break
        rt = bfs(nxt)
        for x in range(n):
            if rt[x]:
                gvisit[x]=1
        answer += 1 
    return answer

"""
네트워크 탐색 -> bfs로 했음 
전체 global visit (gvisit)을 체크하고, 해당 노드를 방문한 적이 없으면 
그 노드를 다음 네트워크 시작으로 bfs를 시작함. 

이후 bfs로 발견한 네트워크로 gvisit을 체크하고 네트워크 갯수를 1 증가 
"""