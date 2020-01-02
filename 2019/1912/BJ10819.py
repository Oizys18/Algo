# 차이최대
import itertools

N = int(input())
nums = list(map(int, input().split()))
res = 0
for i in list(itertools.permutations(nums, N)):
    temp = 0
    for j in range(N-1):
        temp += abs(i[j]-i[j+1])
    if temp > res:
        res = temp
print(res)
