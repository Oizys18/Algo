N = int(input())
res = 0
for i in range(min(N,100),0,-1):
    M = N-i
    nums = [int(j) for j in str(M)]
    sM = sum(nums) + M
    if sM == N:
        res = M
        break
print(res)