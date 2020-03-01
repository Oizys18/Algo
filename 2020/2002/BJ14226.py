# 이모티콘
S = int(input())
res = S+1
visit = [[0]*2000 for _ in range(2001)]
# BFS가 더 빠르다.. .답 나오자 마자 끝내는 거라.. 
def BFS(depth, v, c):
    queue = []
    queue.append((depth,1,0))
    while queue:
        depth, v, c = queue.pop(0)
        if v == S:
            return depth
        if not visit[v][c] or visit[v][c] > depth:
            visit[v][c] = depth
            if depth < res:
                if v != c:
                    queue.append((depth+1,v,v))
                if c and v+c < min(2*S,1001):
                    queue.append((depth+1,v+c, c))
                if 0 < v <= v+c:
                    queue.append((depth+1,v-1,c))
print(BFS(0,1,0))


# def solve(k, v, c):
#     global res
#     if v == S:
#         if k < res:
#             res = k
#         return
#     else:
#         if not visit[v][c] or visit[v][c] > k:
#             visit[v][c] = k
#             if k < res:
#                 if v != c:
#                     solve(k+1, v, v)
#                 if c and v+c < min(2*S,1001):
#                     solve(k+1, v+c, c)
#                 if 0 < v <= v+c:
#                     solve(k+1, v-1, c)
# solve(0, 1, 0)
# print(res)


"""
22
1 0 0
1 1 1
2 1 2
3 1 3
4 1 4 
4 4 5 
8 4 6
12 4 7
11 4 8 
11 11 9
22 11 10
"""
