# BJ2643 
import sys
sys.stdin = open('input2.txt', 'r')
N = int(input()) 
paper = []
for _ in range(N):
    a, b = map(int,input().split())
    if b < a:
        a, b = b, a 
    paper.append((a,b))
paper = sorted(paper)
# print(paper)
flag = 0
res = []
# result = paper[:]    
while paper:
    for i in paper:
        width = i[1]
        for j in paper:  
            if width < j[0]:
                flag = 1
                break 
        if flag == 0:
            res.append(i)
            paper.remove(i)
        flag = 0
        print(paper)

print(res)

# paper = [tuple(map(int,input().split())) for _ in range(N)]
# rSp = list(sorted(paper))
# res = 0
# print(rSp)

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



