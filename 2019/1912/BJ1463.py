# 1로 만들기

N = int(input())
visit = [0]*(10**6+1)
res = N
def solve(k, v):
    global res
    if v == 1:
        if k < res:
            res = k 
        return
    else:
        if k > res:
            return
        if visit[v] and visit[v] <= k:
            return
        else:
            visit[v] = k
            if v % 3 == 0:
                solve(k+1, v//3)
            if v % 2 == 0:
                solve(k+1, v//2)
            solve(k+1, v-1)

solve(0, N)
print(res)