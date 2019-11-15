arr = [1,2,3,4]
N = 3
temp = [0]*N
visit = [0]*N
def perm(k):
    if k == N:
        print(temp)
    else:
        for i in range(N):
            if visit[i]: continue
            temp[k] = arr[i]
            visit[i] = 1
            perm(k+1)
            visit[i] = 0
perm(0)