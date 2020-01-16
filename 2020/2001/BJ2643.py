# 색종이 올려놓기 revisited
# 대전제 : 새로 쌓는 색종이는 이미 쌓은 것들 중 위에 올림
# 조건1 : 새로 올려놓는 종이와 맨 위의 색종이의 변들은 평행한다..
#         (단 90도 돌릴 수 있음)
# 조건2 : 새로 올려 놓는 종이는 아래 종이보다 작거나 같다.
N = int(input())
paper = [sorted(map(int,input().split())) for _ in range(N)]
dp = [0]*N

def solve(p):
    if dp[p]:
        return dp[p]
    dp[p] = 1
    for j in range(N):
        if p != j and paper[p][0] >= paper[j][0] and paper[p][1] >= paper[j][1]:
            dp[p] = max(dp[p], solve(j)+1)
    return dp[p]

for k in range(N):
    dp[k] = solve(k)
print(max(dp))

# print(paper)

# def solve(i):
#     if dp[i]:
#         return dp[i]
#     dp[i] = 1
#     for j in range(N):
#         if i != j and paper[i][0] >= paper[j][0] and paper[i][1] >= paper[j][1]:
#             dp[i] = max(dp[i],solve(j) +1)
#     return dp[i]

# for i in range(N):
#     dp[i] = solve(i)
# print(max(dp))


# res를 만들고,
# 1. res 보다 biggerthan의 값이 작으면 무시
# 2. 크다면 한번 쌓아본다.
# 3. 만약 쌓은 갯수가 res보다 크면 res 갱신

# res = 0

# visit = [0]*N
# dp = [0]*N
# def solve(top, cnt):
#     global res
#     flag = 0
#     if not dp[top]:
#         for i in range(N):
#             if not visit[i] and A_biggerthan_B(top, i) and biggerthan[i]+cnt > res:
#                 visit[i] = 1
#                 solve(i, cnt+1)
#                 visit[i] = 0
#                 flag = 1
#     if not flag:
#         if cnt > res:
#             res = cnt
#         dp[top] = cnt
#         return dp[top]



# for t in range(N):
#     if biggerthan[t] < res:
#         continue
#     else:
#         k = solve(t,0)
# print(dp)



"""
100
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
1 2
8 7
20 10
20 20
15 12
12 14
11 12
15 12
12 14
11 12
"""


# # 색종이 올려놓기
# N = int(input())
# paper = [tuple(map(int,input().split())) for _ in range(N)]
# rSp = list(sorted(paper))
# res = 0

# def DFS(node):
#     global res
#     nodeIdx = rSp.index(node)
#     if node == rSp[0]:
#         if len(visit) > res:
#             res = len(visit)
#         # res.append(len(visit))
#         return
#     else:
#         for i in rSp[0:nodeIdx]:
#             if isSmall(node,i):
#                 visit.append(i)
#                 DFS(i)
#                 visit.pop()

# def isSmall(node, paper):
#     x1, y1 = node
#     x2, y2 = paper
#     if (x2 <= x1 and y2 <= y1) or (x2 <= y1 and y2 <= x1):
#         return True
#     else:
#         return False

# for i in rSp:
#     visit = [i]
#     DFS(i)

# print(res)
