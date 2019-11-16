arr = [1,2,3]
N = 3
R = 2

visit = [0]*N
temp = [0]*R
# 순열 
def perm(k):
    if k == R:
        print(temp)
    else:
        for i in range(N):
            if visit[i]:continue
            visit[i] = 1
            temp[k] = arr[i]
            perm(k+1)
            visit[i] = 0
# perm(0)

# 중복순열 
def perm2(k):
    if k == R:
        print(temp)
    else:
        for i in range(N):
            temp[k] = arr[i]
            perm(k+1)

# perm2(0)



# 조합 
def comb(k,s):
    if k == R:
        print(temp)
    else:
        for i in range(s,N-R+k+1):
            temp[k] = arr[i]
            comb(k+1, i+1)

# comb(0,0)

# 중복조합 
def comb2(k,s):
    if k == R:
        print(temp)
    else:
        for i in range(s,N):
            temp[k] = arr[i]
            comb(k+1, i)
comb2(0,0)