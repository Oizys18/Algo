
#1476.py 날짜계산
E,S,M = map(int,input().split())
def cntYear(E,S,M):
    res = 1
    # res2 = 7980
    while True:
        if res % 15:
            nE = res % 15
        else:
            nE = 15
        if res % 28:
            nS = res % 28
        else:
            nS = 28
        if res % 19:
            nM = res % 19
        else:
            nM = 19

        if nE == E and nS == S and nM == M:
            return res
        res += 1
print(cntYear(E,S,M))


# for i in range(1,7981):
#     print(i%15, i%28, i%19)