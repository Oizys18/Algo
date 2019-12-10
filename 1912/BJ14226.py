# 미해결
S = int(input())
visit = [0]*100
# p = 화면에 있는 이모티콘
# c = 클립보드에 있는 이모티콘

flag = 0
res = 100


def solve(p, c, t):
    global flag
    global res
    if p == S:
        if res > t:
            res = t
        return
    else:
        if t > 2*S:
            return
        if p < S:
            if p+c > c:
                solve(p+c, c, t+1)
            if c <= 2*S:
                solve(p, p+c, t+1)
        if p > S:
            solve(p-1, c, t+1)


solve(1, 0, 0)
print(res)

