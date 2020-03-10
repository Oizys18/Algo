import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint as pp 

def findBest():
    global collections
    global visit
    while True:
        for i in range(N):
            maxNum = max(mat[i])
            zipline = mat2[mat[i].index(maxNum)]
            if (maxNum == max(zipline)):  
                zipIdx = zipline.index(max(zipline))
                oriIdx = mat[i].index(maxNum)
                collections[i] = maxNum
                if collections.count(0) == 0:
                    return collections
                mat[i] = [0]*N
                mat2[oriIdx] = [0]*N
                for j in range(N):
                    mat[j][oriIdx] = 0
                    mat2[j][zipIdx] = 0
                mat[i][oriIdx] = maxNum
                mat2[oriIdx][i] = maxNum

# for T in range(int(input())):
#     N = int(input())
#     mat = [list(map(lambda x : int(x)/100,input().split())) for _ in range(N)]
#     mat2 = [list(i) for i in zip(*mat)]
#     mat3 = copy.deepcopy(mat)
#     collections = [0]*N
#     visit = 0
#     bests = findBest()
#     possbest = 1
#     for b in bests:
#         possbest *= b
#     # print(possbest)
#     res = 0
#     poss = 1
#     temp = []
#     flag = 0


#     # # pp(list(itertools.permutations(range(N),N)))
#     # for i in itertools.permutations(range(N),N):
#     #     print(list(i))
#     for perm in itertools.permutations(range(N),N):        
#         for x in range(N):
#             poss *= mat3[x][perm[x]]
#             # print(poss)
#             # print(possbest)
#             if poss < possbest:
#                 # print('1')
#                 flag = 1
#                 poss = 1
#                 break
#         if flag == 1:
#             flag = 0
#             continue

#         if poss > possbest:
#             possbest = poss 
#             poss = 1
#     # print(possbest)
#     print("#{} {}".format(T+1,format(possbest*100,'.6f')))







# for i in list(itertools.permutations(range(10),5)):
#     print(i)



#     pp(mat2)
#     visit = [0]*N
#     temp = 1
#     for i in mat2:
#         temp *= max(i)/100
#     temp *= 100
#     print(temp)
# """
# """
# # 큰 것부터 하나씩 찾기! 
# visit = [0]*N
# """
    
    
# """    # pp(mat)
# line = [1,2,3,4]
# visit = [0,0,1,1]
# mNum = 0
# for x in range(4):
#     if visit[x] == 0:
#         if line[x] > mNum:
#             mNum = line[x]
# print(mNum)