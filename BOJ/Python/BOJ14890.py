# https://www.acmicpc.net/problem/14890
# 경사로 
import sys
sys.stdin = open('BOJ14890.txt','r')
from pprint import pprint as pp


N,L = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
turned_mat = list(map(list,zip(*mat)))
answer = 0


# i 번째 길을 갈 수 있는지 체크한다.
def check_path(i,mat):
    height = 0
    height_idx = 0 
    bridge = [0]*N
    for x in range(N):

        if not height:
            height = mat[i][x]
            height_idx = x 
        else:
            if height == mat[i][x]:
                height_idx = x 
            elif abs(height-mat[i][x]) > 1:
                return False 
            elif height < mat[i][x]:
                if x-L < 0:
                    return False
                for j in range(x-1,x-L-1,-1):
                    if mat[i][j] != height or bridge[j]:
                        return False
                    else:
                        bridge[j] = 1
                height = mat[i][x]
                height_idx = x
            elif height > mat[i][x]:
                new_height = mat[i][x]
                if x+L > N:
                    return False 
                for j in range(x,x+L):
                    if mat[i][j] != new_height or bridge[j]:
                        return False 
                    else:
                        bridge[j] = 1 
                height = mat[i][x]
                height_idx = x
    return True

for i in range(N):
    answer += check_path(i,mat)
    answer += check_path(i,turned_mat)
print(answer)