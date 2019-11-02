"""
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
edges = {}
line = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
li = list(map(int,line.split()))
for i in range(0,len(li),2):
    if li[i] not in edges.keys():
        edges[li[i]] = []
    if li[i+1] not in edges.keys():
        edges[li[i+1]] = []
    edges[li[i]].append(li[i+1])
    edges[li[i+1]].append(li[i])

visit = [0]*(len(li)+1)
def BFS(node):
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop(0)
        if not visit[node]:
            visit[node] = 1
            print(node)
            for n in edges[node]:
                stack.append(n)
BFS(1)

