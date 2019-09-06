# SWEA1974 스도쿠 검증
import sys
from pprint import pprint
sys.stdin = open('input3.txt','r')
for T in range(int(input())):
    mat = [list(map(int,input().split())) for _ in range(9)]
    temp = [[0]*10 for _ in range(9)]
    # 네모
    for x in range(9):
        for y in range(9):
            if 0 <= x <= 2:
                if 0 <= y <= 2:
                    temp[0][mat[x][y]] = 1
                elif 3 <= y <= 5: 
                    temp[1][mat[x][y]] = 1
                elif 6 <= y <= 8:
                    temp[2][mat[x][y]] = 1 
            elif 3 <= x <= 5: 
                if 0 <= y <= 2:
                    temp[3][mat[x][y]] = 1 
                elif 3 <= y <= 5:
                    temp[4][mat[x][y]] = 1 
                elif 6 <= y <= 8: 
                    temp[5][mat[x][y]] = 1
            elif 6 <= x <= 8: 
                if 0 <= y <= 2: 
                    temp[6][mat[x][y]] = 1
                elif 3 <= y <= 5: 
                    temp[7][mat[x][y]] = 1
                elif 6 <= y <= 8: 
                    temp[8][mat[x][y]] = 1
    res = 1
    for r in temp:
        if sum(r) != 9:
            res = 0
    temp = [[0]*10 for _ in range(9)]
    
    # 가로줄 
    for x in range(9):
        for y in range(9):
            temp[x][mat[x][y]] = 1
    for r in temp:
        if sum(r) != 9:
            res = 0
    temp = [[0]*10 for _ in range(9)]

    mat = list(zip(*mat))
    for x in range(9):
        for y in range(9):
            temp[x][mat[x][y]] = 1
    for r in temp:
        if sum(r) != 9:
            res = 0
    print("#{} {}".format(T+1,res))