# SWEA 4875 미로
import sys
sys.stdin = open('input3.txt','r')
def bt(start):
    stack = []
    visit = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if pathFinder(node):
                stack.extend(pathFinder(node))
    return visit

def pathFinder(x,y):
    path = []
    if y > 0 and y < N - 1:
        while y > 0 and y < N - 1:
            if x > 0 and x < N - 1 :
                while x > 0 and y < N - 1:
                    

            
            




    return path
    
    
    
    
    
    #adj_list = [mat[node[0]+1][node[1]],mat[node[0]][node[1]+1],mat[node[0]][node[1]-1]]

    # 우, 하 탐색
    # if node[1] == 0:
    #     if mat[node[0]][node[1]+1] in '02':
    #         zeros.append((node[0],node[1]+1))
    #     if mat[node[0]+1][node[1]] in '02':
    #         zeros.append((node[0]+1,node[1]))
    # elif node[1] == N-1:
    #     if mat[node[0]][node[1]-1] in '02':
    #         zeros.append((node[0],node[1]-1))
    #     if mat[node[0]+1][node[1]] in '02':
    #         zeros.append((node[0]+1,node[1]))

    # elif node[0] == N-1:
    #     if mat[node[0]][node[1]+1] in '02':
    #         zeros.append((node[0],node[1]+1))
    #     if mat[node[0]][node[1]-1] in '02':
    #         zeros.append((node[0],node[1]-1))
    # else:
    #     if mat[node[0]][node[1]+1] in '02':
    #         zeros.append((node[0],node[1]+1))
    #     if mat[node[0]+1][node[1]] in '02':
    #         zeros.append((node[0]+1,node[1]))
    #     if mat[node[0]][node[1]-1] in '02':
    #         zeros.append((node[0],node[1]-1))
    # return zeros





for T in range(int(input())):
    stack = []
    N = int(input())
    
    mat = [input() for _ in range(N)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '3':
                start = (i,j)
            if mat[i][j] == '2':
                end = (i,j)
    print(start, end)

    res = [mat[i[0]][i[1]] for i in bt(start)]

    result = 0
    for j in res:
        if j == '2':
            result = 1

    print("#{0} {1}".format(T+1,result))
    





