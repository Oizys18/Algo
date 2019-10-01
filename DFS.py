edges = {
    1:[2,3,4],
    2:[5,6],
    3:[7],
    4:[8],
    5:[9],
    6:[10],
    7:[],
    8:[],
    9:[],
    10:[11],
    11:[],
}


def DFS(node):
    if len(edges[node]) == 0:
        print(visit)
        return
    else:
        for i in edges[node]:
            visit.append(i)
            DFS(i)
            visit.pop()

for i in edges.keys():
    visit = [i]
    DFS(i)
    