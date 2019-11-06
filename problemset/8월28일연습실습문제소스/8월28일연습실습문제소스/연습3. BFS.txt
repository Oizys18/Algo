G = [
 [ 0, 0, 0 ],
 [ 2, 3, 0 ],   #정점 1의 인접정점
 [ 1, 4, 5 ],   #정점 2의 인접정점
 [ 1, 7, 0 ],   #정점 3의 인접정점
 [ 2, 6, 0 ],   #정점 4의 인접정점
 [ 2, 6, 0 ],   #정점 5의 인접정점
 [ 4, 5, 7 ],   #정점 6의 인접정점
 [ 3, 6, 0 ]]   #정점 7의 인접정점

q = [0] * 10
visited = [0] * 8

def BFS(w):
    f = r = -1
    r += 1; q[r] = w

    print("%d"%q[r])
    visited[w] = 1;

    while f != r:
        f += 1; w = q[f]
        for i in range(3):
            if G[w][i] and not visited[G[w][i]]:
                r += 1; q[r] = G[w][i]
                print("%d"%q[r])
                visited[G[w][i]] = 1

BFS(1)

