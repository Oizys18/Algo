#시험감독

N = int(input())
test = list(map(int,input().split()))
temp = [0]*N
B, C = map(int,input().split())

res = 0
for i in range(N):
    temp[i] += B
    res += 1
    while temp[i] < test[i]:
        temp[i] += C
        res += 1
print(res)