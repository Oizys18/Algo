from copy import deepcopy as dc
from pprint import pprint as pp
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], [
    'SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]


def solution(tickets):
    answer = []
    db = dict()
    for idx, ticket in enumerate(tickets):
        if not db.get(ticket[0]):
            db[ticket[0]] = []
        # 출발지에는 안나오고 도착지에만 나오는 공항이 존재한다!
        if not db.get(ticket[1]):
            db[ticket[1]] = []
        db[ticket[0]].append((idx, ticket[1]))

    used = [0]*len(tickets)
    possible_route = []

    def DFS(node, arr):
        if len(arr) == len(tickets)+1:
            possible_route.append(dc(arr))
            return
        if len(db[node]) == 0:
            return
        else:
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
print(solution(tickets))
