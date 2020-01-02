def solve(k, s):
    global res
    if k == R:
        start = 0
        link = 0
        temp2 = list(set([j for j in range(N)])-set(temp))
        # print(temp, temp2)
        for x in range(R-1):
            for y in range(x+1,R):
                start += (mat[temp[x]][temp[y]] + mat[temp[y]][temp[x]])
        for x in range(R-1):
            for y in range(x+1,R):
                link += (mat[temp2[x]][temp2[y]] + mat[temp2[y]][temp2[x]])
        res = min(res, abs(start-link))
    else:
        for i in range(s,N-R+k+1):
            temp[k] = i
            solve(k+1, i+1)

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

R = N//2
res = 1e9
temp = [0]*R
solve(0,0)
print(res)

# 강사님 
def solve(k, s):
    global ans
    if k == R:
        start = link = 0
        x = list(set([x for x in range(N)]) - set(t))
        print(t,x)
        # print()
        for i in range(R - 1):
            for j in range(i + 1, R):
                start += (mat[t[i]][t[j]] + mat[t[j]][t[i]])
        for i in range(R - 1):
            for j in range(i + 1, R):
                link += (mat[x[i]][x[j]] + mat[x[j]][x[i]])

        ans = min(ans, abs(start - link))

    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = i
            solve(k + 1, i + 1)


N = int(input())
R = N // 2
t = [0] * R
mat = [list(map(int, input().split())) for _ in range(N)]

ans = 1e9
solve(0, 0)

print(ans)
