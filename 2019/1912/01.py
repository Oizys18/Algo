# 문제1 : 칠 영역의 개수 구하기

# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    colorDic = {}
    mat = [[0 for _ in range(N)] for _ in range(N)]
    point = []
    for i in range(1,M+1):
        colorDic[i] = []
        paint = list(map(int,input().split()))
        point = [colorDic[i].append((paint[k], paint[k+1])) for k in range(0,len(paint),2)]

    for j in range(1,len(colorDic)+1):
        a = colorDic[j][1][0] - colorDic[j][0][0] + 1
        b = colorDic[j][1][1] - colorDic[j][0][1] + 1 
        for k in range(a):
            for l in range(b):
                mat[colorDic[j][0][0] - 1+k][colorDic[j][0][1] - 1 + l] = 1
    res = 0
    for r in mat:
        res += sum(r)
    print("#{0} {1}".format(t+1,res))
