# SWEA 4828 min max
# N개의 양의 정수 중 가장 큰 수와 가장 작은 수의 차이를 출력


for case in range(int(input())):
    #N length
    nl = int(input())
    ai = list(map(int,input().split()))
    for i in range(nl-1,0,-1):
        for j in range(0,i):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]
    result = ai[nl-1] - ai[0]
    print("#{0} {1}".format(case+1,result))