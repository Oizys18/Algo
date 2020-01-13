# 색종이 올려놓기 revisited













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
