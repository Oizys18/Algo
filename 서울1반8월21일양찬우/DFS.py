dfsMat = [
[0,1,1,0,0,0,0],
[1,0,0,1,1,0,0],
[1,0,0,0,0,0,1],
[0,1,0,0,0,1,0],
[0,1,0,0,0,1,0],
[0,0,0,1,1,0,1],
[0,0,1,0,0,1,0],
]

dfsDic = {
    1: [2,3],
    2: [4,5],
    3: [1,7],
    4: [2,6],
    5: [2,6],
    6: [4,5,7],
    7: [3,6],
}



def dfs(graph, start_node):
    visit = []
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

print(dfs(dfsDic,1))