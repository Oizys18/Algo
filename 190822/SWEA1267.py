#SWEA1267
import sys
sys.stdin = open("input.txt",'r')




#나
for T in range(1,11):
    V,E = map(int,input().split())
    matN = list(map(int,input().split()))
    mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        mat[matN[2*i]][matN[2*i+1]] = 1
    reMat= list(map(list, zip(*mat)))
    visited = []
    queue = []
    connect = {}
    stack = []

    for j in range(1,len(reMat)):
        connect[j] = sum(reMat[j])
        if connect[j] == 0 :
            queue.append(j)
            stack.append(j)
    # # dfs 
    while len(queue) != 0: 
        node = queue.pop()
        visited.append(node)
        for k in range(1,len(mat[node])):
            if mat[node][k] == 1:
                connect[k] -= 1
        for j in connect:  
            if connect[j] == 0 and j not in stack:
                queue.append(j)
                stack.append(j)
                
    print("#{0}".format(T),end=' ')
    for i in visited:
        print("{0}".format(i),end=' ')
    print()




