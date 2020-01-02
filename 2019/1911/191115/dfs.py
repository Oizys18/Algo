# DFS
G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [0] * 8

# Stack 사용
def dfs(start):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            print(node)
            # print(visited)
            for i in G[node]:
                if not visited[i]:
                    stack.append(i)

# 재귀
def dfs2(node):
    visited[node]=1
    print(node)
    for i in G[node]:
        if not visited[i]:
            dfs2(i)

# dfs(1)
# dfs2(1)



