# BJ2651 자동차경주
# gas = int(input())
# N = int(input())
# far = [*map(int, input().split())]
# time = [*map(int, input().split())]
# visit = [0]*(N+2)
# resvisit = []
# res = sum(time)

# def solve(k, t):
#     global visit
#     global resvisit
#     global res
#     if k == N+1:
#         if t < res:
#             res = t
#             resvisit = visit.copy()
#         return
#     else:
#         # k 부터 시작
#         reach = 0
#         for i in range(k+1, N+2):
#             reach += far[i-1]
#             if reach <= gas and not visit[i]:
#                 visit[i] = 1
#                 solve(i,t+time[i-1])
#                 visit[i] = 0
# solve(0,0)

# print(res)
# cnt = 0
# for k in resvisit:
#     if k:
#         cnt += 1
# print(cnt)
# if cnt != 0:
#     for k in range(len(resvisit)):
#         if resvisit[k]:
#             print(k,end=' ')

# """
# 140
# 5
# 0 0 0 0 0 0
# 5 10 4 11 7
# """


# ??? 말렸다 !
gas = int(input())
stops = int(input())
visit = [0]*(stops+2)
far = [0]+ [*map(int, input().split())] 
cost = [0] + [*map(int, input().split())] + [0]


resC = sum(cost)
resV = []
# current stop, cost
def solve(s, c):
    global resC
    global resV
    if s == stops+1:
        if c < resC:
            print(visit)
            resC = c
            resV = visit.copy()
        return
    else:
        for stop in range(stops+1,s,-1):
            used = sum(far[s+1:stop+1])
            if used <= gas and not visit[stop]:
                if c + cost[stop] < resC:
                    visit[stop] = 1
                    solve(stop, c+ cost[stop])
                    visit[stop] = 0
solve(0, 0)
print(resC)
cnt = sum(resV)-1
print(cnt)
if cnt:
    for v in range(len(resV)-1):
        if resV[v]:
            print(v,end=' ')

"""
140
15
100 30 100 40 50 60 100 30 100 40 50 60 100 30 100 40 50 60
5 10 4 11 7 5 10 4 11 7 5 10 4 11 7
"""
