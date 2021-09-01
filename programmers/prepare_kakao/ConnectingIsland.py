from collections import defaultdict
from heapq import * 
def solution(n, costs):
    answer = 0
    costs.sort()
    nodes = defaultdict(list)
    for n1,n2,cost in costs:
        nodes[str(n1)].append((cost,str(n1),str(n2)))
        nodes[str(n2)].append((cost,str(n2),str(n1)))
    start = str(costs[0][0])
    connected = set(start)
    adjNodes = nodes[start]
    heapify(adjNodes)
    
    while adjNodes:
        cost,n1,n2 = heappop(adjNodes)
        if n2 not in connected:
            connected.add(n2)
            answer += cost
            for node in nodes[n2]:
                if node[2] not in connected:
                    heappush(adjNodes,node)
    return answer


"""
리스트 들어오면 무조건 소트 한번 할 것 
소트 없이 line10으로 했다가 안됐음.
순서 상관없이 무조건 첫번째로 들어오는 섬에서 시작하는 것으로 설정했던 건데, 
생각해보니 들어오는 costs는 연결(다리)이고, 처음 들어오는 연결이 만약 필요없는 (하지 말아야할)연결이라면 에러가 날 수 밖에 없음. 
"""