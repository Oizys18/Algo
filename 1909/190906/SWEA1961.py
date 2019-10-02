# SWEA1961
import sys
from pprint import pprint
sys.stdin = open('input6.txt','r')

for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mat1 = list(zip(*mat))
    mat2 = list(reversed(mat))
    for i in range(len(mat2)):
        mat2[i] = list(reversed(mat2[i]))
    mat3 = list(zip(*mat))
    print('#{}'.format(T+1))
    for x in range(N):
        for y3 in range(N-1,-1,-1):
            print(mat3[x][y3],end='')
        print(' ',end='')
        for y2 in range(N):
            print(mat2[x][y2],end='')
        print(' ',end='')
        for y3 in range(N):
            print(mat3[N-x-1][y3],end='')
        print()
        
        

    
    # # 테스트 출력 
    # print(mat)
    # print()
    # print(mat2)
    # print()
    # print(mat3)


"""
1
3
1 2 3
4 5 6
7 8 9
"""