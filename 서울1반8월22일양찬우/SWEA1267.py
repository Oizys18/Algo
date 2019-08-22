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
            
    visited = [False] * (V+1)
    visited[v]
                



"""
#갓상우.. 
def dfs(v):
    visit[v] = 1
    [dfs(w) for w in adj_list[v] if not visit[w]]
    ans.append(v)
 
for t in range(10):
    V, E = map(int, input().split())
    *info, = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for i in range(0, 2 * E, 2):
        adj_list[info[i + 1]].append(info[i])
    ans = []
    visit = [0] * (V + 1)
    [dfs(i) for i in range(1, V + 1) if not visit[i]]
    print(f"#{t+1} {' '.join(map(str, ans))}")


"""



def dfs(graph, start_node):
    visit = []
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph)
    return visit

for T in range(3):
    V,E = map(int,input().split())
    matN = list(map(int,input().split()))
    mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        mat[matN[2*i+1]][matN[2*i]] = 1
    reMat= list(map(list, zip(*mat)))
    dfsDic = {}
    end = []

    for j in range(1,len(reMat)):
        if reMat[j]==1:
            dfsDic[j] = j
        if dfsDic[j] == 0 :
            end.append(j)

    for k in end:
        print(dfs(dfsDic,k))
