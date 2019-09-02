# SWEA4881

"""
N x N 배열 
한 줄 하나의 숫자 
N개의 숫자의 합이 최소가 되도록 하기 
단 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
"""
import sys
sys.stdin = open('input4.txt','r')

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

for T in range(int(input())):
    N = int(input())
    mat = []
    Nl = []
    for n in range(N):
        mat.append(list(map(int,input().split())))
        Nl.append(n)

    perm = permute(Nl)
    # sum_li = []
    # for i in perm:
    #     temp = []
    #     for j in range(N):
    #         temp.append(mat[j][i[j]])
    #     sum_li.append(sum(temp))
    # print("#{0} {1}".format(T+1, min(sum_li)))
    print(perm)





