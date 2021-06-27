import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]
pp(mat)

# 기준점 x,y와 d1,d2가 정해지면 선거구가 결정됨 
for x in range(N):
    for y in range(N):
        if y == 0 or y==N-1 or x >= N-2:
            continue
        check = [[0]*N for _ in range(N)]
        for d1 in range(1,N-x-1):
            for d2 in range(1,N-x-d1):
                # x,y에서 d1 만큼 좌하단, d2만큼 우하단, d1만큼 우상단, d2만큼 좌상단 이동 
                top =(x,y)
                left = (x+d1,y-d1)
                bottom = (x+d1+d2,y-d1+d2)
                right = (x+d2,y+d2)
                # one = 0
                # two = 0
                # three = 0
                # four = 0 
                # five = 0 

                print(x,y,d1,d2,'-------------------')
                print(top,left,bottom,right,N-x-d1-1)
                for r in range(N):
                    for c in range(N):
                        if 0 <= r <left[0] and 0<=c<=top[1]:
                            check[r][c] = 1
                        elif 0<= r <= right[0] and top[1] < c <N:
                            check[r][c] = 2
                        elif left[0]<= r <N and 0<= c < bottom[1]:
                            check[r][c] = 3
                        elif right[0]< r < N and bottom[1]<= c < N : 
                            check[r][c] = 4
                check[top[0]][top[1]] = 5
                check[left[0]][left[1]] = 5
                check[right[0]][right[1]] = 5
                check[bottom[0]][bottom[1]] = 5

                pp(check)



# def paint(x,y,d1,d2):
    




# 기준점 x,y 
def solve(x,y):
    # return 넓이차 
    pass