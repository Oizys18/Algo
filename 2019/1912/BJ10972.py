# 다음 순열
N = int(input())
perm = list(map(int,input().split()))

def next_perm(perm):
    this = 0
    flag = 0

    for i in range(N-1):
        if perm[i] < perm[i+1]:
            this = i
            flag = 1

    if flag:
        cut = perm[this:]

        # 중간 
        if len(cut) > 2:
            tail = sorted(cut[1:])
            nextk = 0
            for k in range(len(tail)):
                if tail[k] > cut[0]:
                    nextk = k
                    break
            res = perm[0:this] + [tail[nextk]] + sorted([cut[0]] +tail[0:nextk] + tail[nextk+1:])

            return res
        # 마지막 두자리 
        else:
            perm[i], perm[i+1] = perm[i+1], perm[i]
            return perm
    else:
        return -1

resPerm = next_perm(perm)
if resPerm != -1:
    for p in resPerm:
        print(p,end=' ')
    print()
else:
    print(resPerm)




"""
# 메모리 초과 
import itertools

perms = itertools.permutations(range(1,N+1),N)
for i in list(itertools.permutations(range(1,N+1),N)):
    if count == this:
        for k in i:
            print(k,end=' ')
        print()
    if i == perm:
        this = count + 1
    count += 1
else:
    print(-1)
"""
"""

1. 앞에서부터 뒤의 값과 비교 
2. 만약 앞의 값보다 뒤의 값이 크다면 저장 
3. 그러면 결국 뒤의 값이 더 큰 수 중 마지막 인덱스 저장됨
4. 해당 인덱스부터 끝까지 자르기 array[i:]
5-1 자른 값의 길이가 2면 자리 바꾸고 출력 
5-2 길이가 2 이상이면 해당 인덱스의 값보다 1 큰 수로 바꾸고 나머지 정렬 

"""


