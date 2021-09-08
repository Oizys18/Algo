from collections import defaultdict
def solution(n, edge):
    answer = 0
    edges = defaultdict(list)
    for a,b in edge:
        edges[a].append(b)
        edges[b].append(a)
                
    def bfs(start):
        visit = [0]*(n+1)
        q = [(start,1)]
        visit[start] = 1 
        while q:
            cur_node,cur_depth = q.pop(0)
            for node in edges[cur_node]:
                if not visit[node]:
                    q.append((node,cur_depth+1))
                    visit[node] = cur_depth+1 
        return visit 
    
    rt = bfs(1)
    mx = max(rt)
    for i in rt:
        if i == mx:
            answer += 1 

    return answer

"""
처음에 cur_node,cur_depth pop 이후 visit을 했더니 
큐에 쌓여서 중복 노드를 재방문 했을 시 depth가 더 낮으면 visit을 갱신하는 방식으로 썼다. 
-> 시간초과 

생각해보니까 그냥 q에 넣으면서 visit 체크하고 depth 넣으면 가장 작은 depth 값으로 넣는 셈이라서 해당 방식으로 해결했다. 
"""