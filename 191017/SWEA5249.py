import sys
sys.stdin = open('input.txt','r')
# import queue

for T in range(int(input())):
    V, E = map(int,input().split())  
    edges = []
    for _ in range(E):
        n1, n2, w = map(int,input().split())
        edges.append((w,n1,n2))
    edges.sort()

    parent = {}
    rank = {}
    def MakeSet(x):
        parent[x] = x
        rank[x] = 0

    def FindSet(x):
        if x != parent[x]:
            parent[x] = FindSet(parent[x])
        return parent[x]

    def Union(x, y):
        rootX = FindSet(x)
        rootY = FindSet(y)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
                
                if rank[rootX] == rank[rootY]:
                    rank[rootY] += 1
    for i in range(V+1):
        MakeSet(i)
    result = []
    for edge in edges:
        w, n1, n2 = edge
        if FindSet(n1) != FindSet(n2):
            Union(n1, n2)
            result.append(w)
    print(f"#{T+1} {sum(result)}")