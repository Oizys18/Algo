# RGB거리
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
choice = [-1]*N
res = 3e6

def solve(k, s):
    global res
    if k == N:
        if s < res:
            res = s
        return
    else:
        if k == 0:
            choice[k] = 0
            solve(k+1,s+mat[k][choice[k]])
            choice[k] = 1
            solve(k+1,s+mat[k][choice[k]])
            choice[k] = 2
            solve(k+1,s+mat[k][choice[k]])
        else:
            if choice[k-1] == 0:
                choice[k] = 1
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
                choice[k] = 2
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
            elif choice[k-1] == 1:
                choice[k] = 0
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
                choice[k] = 2
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
            elif choice[k-1] == 2:
                choice[k] = 0
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
                choice[k] = 1
                if res > s + mat[k][choice[k]]:
                    solve(k+1,s+mat[k][choice[k]])
solve(0,0)
print(res)