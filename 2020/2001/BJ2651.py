# BJ2651 자동차경주
gas = int(input())
stops = int(input())
visit = [0]*(stops+2)
far = [0]+ [*map(int, input().split())] 
cost = [0] + [*map(int, input().split())] + [0]














# resC = sum(cost)
# resV = []

# # current stop, cost
# def solve(s, c):
#     global resC
#     global resV
#     if s == stops+1:
#         if c < resC:
#             print(visit)
#             resC = c
#             resV = visit.copy()
#         return
#     else:
#         for stop in range(stops+1,s,-1):
#             used = sum(far[s+1:stop+1])
#             if used <= gas and not visit[stop]:
#                 if c + cost[stop] < resC:
#                     visit[stop] = 1
#                     solve(stop, c+ cost[stop])
#                     visit[stop] = 0
# solve(0, 0)
# print(resC)
# cnt = sum(resV)-1
# print(cnt)
# if cnt:
#     for v in range(len(resV)-1):
#         if resV[v]:
#             print(v,end=' ')

# """
# 140
# 15
# 100 30 100 40 50 60 100 30 100 40 50 60 100 30 100 40 50 60
# 5 10 4 11 7 5 10 4 11 7 5 10 4 11 7
# """



# # 자동차경주..revisited..
# gas = int(input())
# stops = int(input())
# visit = [0]*(stops+2)
# far = [0]+ [*map(int, input().split())] 
# cost = [0] + [*map(int, input().split())] + [0]

