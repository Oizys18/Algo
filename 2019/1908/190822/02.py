# 문제2 : 최대 사각 테두리의 합 구하기

import sys
sys.stdin = open('input2.txt','r')

for T in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    # 행렬 생성 및 값 입력
    mat = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        n = list(map(int,input().split()))
        for j in range(len(n)):
            mat[i][j] = n[j]

    sum_li = []
    temp = []
    # 도넛 이동 제한 
    for l in range(N-K+1): 
        for k in range(M-K+1):
            for i in range(K):
                for j in range(K):
                    temp.append(mat[l+i][k+j])
            for i in range(K-2):
                for j in range(K-2):
                    temp.remove(mat[l+1+i][k+1+j])
            sum_li.append(sum(temp))
            #temp reset
            temp = []
    
    result = max(sum_li)
    print("#{0} {1}".format(T,result))