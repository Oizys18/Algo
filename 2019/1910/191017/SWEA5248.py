# 조합 
import sys
sys.stdin = open('input7.txt','r')

for T in range(int(input())):
    N, M = map(int,input().split())
    check = list(map(int,input().split()))
    edges = {}
    for i in range(1,N+1):
        edges[i] = []
    for j in range(M):
        edges[check[2*j]].append(check[2*j+1])
        edges[check[2*j+1]].append(check[2*j])
    group = 1
    visit = [0]*(N+1)
    def BFS(node):
        global group
        global visit
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop(0)
            if not visit[node]:
                visit[node] = group
                if edges[node]:
                    for n in set(edges[node]):
                        queue.append(n)
    for k in range(1,N+1):
        BFS(k)
        group += 1
    print(f"#{T+1} {len(set(visit))-1}")



"""
# 결국 그냥 BFS로 group의 갯수를 세는 방식을 썼다
# 조합을 만드는 방법에 문제가 있는듯..?
"""



"""
    # 이렇게하면 각각 조가 만들어진 이후에 상대방 조랑 합치는 걸 못해줌. 
    # Disjoint set으로 만들어야함 

    zo = [0]*(N+1)
    cnt = 1
    flag = 0
    for i in range(M): 
        for j in range(1,len(zo)):
            if zo[j]:
                if checkList[2*i] in zo[j]:
                    zo[j].add(checkList[2*i+1])
                    flag = 1
                elif checkList[2*i+1] in zo[j]:
                    zo[j].add(checkList[2*i])
                    flag = 1
        if flag:
            flag = 0
        else:
            zo[cnt]={checkList[2*i]}
            zo[cnt].add(checkList[2*i+1])
            flag = 0
            cnt += 1
    for k in range(1,N+1):
        if k not in checkList:
            zo[cnt] = {k}
            cnt += 1
    res = 0
    print(zo)
    for li, l in enumerate(zo):
        for mi, m in enumerate(zo):
            if l and m and l != m:
                if not l.isdisjoint(m):
                    zo[li]=l.union(m)
                    zo[mi]= 0
    for o in zo:
        if o:
            res += 1


    # print(zo)
    print(f"#{T+1} {res}")
"""



