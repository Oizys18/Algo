# 이모티콘 
S = int(input())
res = 100
def solve(k, v, c):
    global res
    if v == S:
        if k < res:
            res = k
            print(k)
        return
    else:
        # clipboard
        if v < S:
            if v != c:
                solve(k+1, v, v)
            # paste 
            if c != 0:
                solve(k+1, v+c, c)
        # delete
        if v:
            solve(k+1, v-1, c)

solve(0, 1, 0)

