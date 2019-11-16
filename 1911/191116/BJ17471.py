import itertools


# def dfs(v, area, visited):
#     ret = people[v]
#     visited[v] = 1
#     for u in G[v]:
#         if not visited[u - 1] and u - 1 in area:
#             ret += dfs(u - 1, area, visited)
#     return ret


# def solve(k):
#     global ans
#     if k == N:
#         if sum(subset) == 0 or sum(subset) == N: return

#         area1, area2 = [], []
#         for i in range(N):
#             if subset[i]:
#                 area1.append(i)
#             else:
#                 area2.append(i)
#         visited = [0] * N
#         v1 = dfs(area1[0], area1, visited)
#         v2 = dfs(area2[0], area2, visited)
#         if sum(visited) == N:
#             ans = min(ans, abs(v1 - v2))
#     else:
#         subset[k] = 1; solve(k + 1)
#         subset[k] = 0; solve(k + 1)


# N = int(input())
# pop = [i for i in range(1,N+1)]
# people = list(map(int, input().split()))
# G = []

# for i in range(N):
#     tlist = list(map(int, input().split()))
#     G.append(tlist[1:])

# ans = 1e9
# subset = [0] * N
# solve(0)
# if ans == 1e9:
#     print(-1)
# else:
#     print(ans)

# N = 10
# for i in itertools.chain.from_iterable(itertools.combinations(range(1,N+1),r) for r in range(1,N+1)):
#     print(i)

# temp = [0]*3
# def powerset2(s):
#     x = len(s)
#     for i in range(1 << x):
#         for j in range(x):
#             if i & (1 << j):
#                 temp[j] = s[j]
#             else:
#                 temp[j] = 0
#         print(temp)
#         # print([s[j] for j in range(x) if (i & (1 << j))])

# powerset2([1,2,3])


# def powerset(N):
#     temp = [0]*N
#     for i in range(1 << N):
#         for j in range(N):
#             if i & (1 << j):
#                 print(pop[j])
#         # print(temp) 
# powerset(3)

N = 3

for i in itertools.chain.from_iterable(itertools.combinations(range(1,N+1),r) for r in range(1,N)):
    print(i)