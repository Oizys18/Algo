M, N = map(int,input().split())
visited = [0]*100001
def pathfinder(node):
    if 0 <= node <= 100000:
        return True
    else:
        return False

def BFS(depth, node):
    queue = []
    queue.append((0,node))
    while queue:
        depth, node = queue.pop(0)
        if node == N:
            return depth
        if not visited[node]:
            visited[node] = 1
            if pathfinder(node-1):
                queue.append((depth+1,node-1))
            if pathfinder(node+1):
                queue.append((depth+1,node+1))
            if pathfinder(node*2):
                queue.append((depth+1,node*2))    

print(BFS(0,M))
