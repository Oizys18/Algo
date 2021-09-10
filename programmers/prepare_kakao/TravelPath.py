def solution(tickets):
    answer = []
    db = dict()
    for idx, ticket in enumerate(tickets):
        if not db.get(ticket[0]):
            db[ticket[0]] = []
        if not db.get(ticket[1]):
            db[ticket[1]] = []
        db[ticket[0]].append((idx, ticket[1]))

    used = [0]*len(tickets)
    possible_route = []

    def DFS(node, arr):
        if len(arr) == len(tickets)+1:
            possible_route.append([x for x in arr])
            return
        if len(db[node]) == 0:
            return
        for idx, next_airport in enumerate(db[node]):
            if used[next_airport[0]]:
                continue
            used[next_airport[0]] = 1
            arr.append(next_airport[1])
            DFS(next_airport[1], arr)
            arr.pop()
            used[next_airport[0]] = 0

    DFS('ICN', ['ICN'])
    
    answer = sorted(possible_route)[0]
    return answer


def solution(tickets):
    answer = []
    N = len(tickets)
        
    def dfs(k,visit,route):
        if k == N:
            answer.append(route.copy())
            return 
        else:
            for i in range(N):
                if not visit[i] and route[-1] ==tickets[i][0]:
                    visit[i] = 1 
                    route.append(tickets[i][1])
                    dfs(k+1,visit,route)
                    route.pop()
                    visit[i] = 0 
                    
    dfs(0,[0]*N,['ICN'])
    return sorted(answer)[0]
"""
이-지
"""