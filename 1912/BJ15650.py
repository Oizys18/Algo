# N과 M(2)
N, M = map(int, input().split())
visited = [0]*N
arr = range(1, N+1)
temp = [0]*M


def perm(k):
    if k == M:
        if temp == sorted(temp):
            for t in temp:
                print(t, end=' ')
            print()
        return
    else:
        for i in range(N):
            if visited[i]:
                continue
            temp[k] = arr[i]
            visited[i] = 1
            perm(k + 1)
            visited[i] = 0


perm(0)
