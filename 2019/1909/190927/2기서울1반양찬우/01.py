import sys
sys.stdin=open('input.txt','r')

def cntSame(li1, li2, dot):
    li = li1 + li2
    li.remove(dot)
    numDic = {}
    temp = 0
    big = 0
    for j in set(li):
        numDic[j] = li.count(j)
        if li.count(j) > temp:
            temp = li.count(j)
            big = j
    res = 0
    for k in numDic.keys():
        res += abs(k - big) * numDic[k]
    return res, big

for T in range(int(input())):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mat2 = [list(i) for i in zip(*mat)]
    result = 5000
    resH = 0
    for x in range(N):
        lineX = mat[x]
        for y in range(N):
            lineY = mat2[y]
            dotRes, height = cntSame(lineX, lineY, mat[x][y])
            if dotRes < result:
                result = dotRes
                resH = height
            elif dotRes == result:
                resH = height
    print("#{} {} {}".format(T+1, result, resH))
