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
#         print(area1)
#         print(area2)
#         # visited = [0] * N
#         # v1 = dfs(area1[0], area1, visited)
#         # v2 = dfs(area2[0], area2, visited)
#         # if sum(visited) == N:
#         #     ans = min(ans, abs(v1 - v2))
#     else:
#         subset[k] = 1; solve(k + 1)
#         subset[k] = 0; solve(k + 1)


# N = int(input())
# people = list(map(int, input().split()))
# G = []

# for i in range(N):
#     tlist = list(map(int, input().split()))
#     G.append(tlist[1:])

# ans = 1e9
# subset = [0] * N
# solve(0)
# # if ans == 1e9:
# #     print(-1)
# # else:
# #     print(ans)
arr = [1,2,3,4]
N = 4

for i in range(1 << N):
    subset = []
    subset2 = []
    for j in range(N):
        if j == 0 or j == N-1:continue
        if i & ( 1 << j):
            subset.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset)
    print(subset2)
    print()



# x = 3
# temp = [0]*x
# for i in range(1 << x):
#     for j in range(x):
#         if i & (1 << j):
#             temp[j] = 1
#         else:
#             temp[j] = 0
#     print(temp)