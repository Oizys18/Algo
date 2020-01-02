#시험감독

N = int(input())
test = list(map(int,input().split()))
B, C = map(int,input().split())
temp = [B]*N

res = N
for i in range(N):
    if temp[i] < test[i]:
        if test[i] - temp[i] > C:
            if (test[i] - temp[i]) % C == 0:
                res += (test[i] - temp[i]) // C
            else:
                res += (test[i] - temp[i]) // C + 1
        else:
            res += 1
print(res)



