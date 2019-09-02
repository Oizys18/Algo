# SWEA 4836 색칠
import sys
sys.stdin = open('input.txt', 'r')

"""
dictionary를 통해 {color:(좌표)}로 추가, set 후 교집합 -> list로 겹친 좌표 수를 확인 
"""
for T in range(int(input())):
    squs = []
    N = int(input())
    dict_col = {1:[],2:[]}
    for k in range(N):
        squs.append(list(map(int, input().split())))
        for i in range(squs[k][2]-squs[k][0] + 1):
            for j in range(squs[k][3]-squs[k][1]+1):
                dict_col[squs[k][4]].append((squs[k][0] + i, squs[k][1] + j))
    print("#{0} {1}".format(T+1,len(set(dict_col[1]) & set(dict_col[2]))))
    dict_col = {}