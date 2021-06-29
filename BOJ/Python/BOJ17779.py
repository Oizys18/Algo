import sys
sys.stdin = open('BOJ17779.txt','r')
from pprint import pprint as pp
# 게리맨더링2
N = int(input())
mat =[[*map(int,input().split())] for _ in range(N)]
# dr = [(1,-1),(1,1),(-1,1),(-1,-1)]





# 기준점 x,y와 d1,d2가 정해지면 선거구가 결정됨 
check = [[0]*N for _ in range(N)]
for x in range(N-2):
    for y in range(1,N-1):
        check[x][y] = 1 
        # 
pp(check)
        # if (y == 0 or y==N-1) or x >= N-2:
        #     continue
        # for d1 in range(1,min(y+1,N-x-1)):
        #     # print(min(N-x-d1+1,N-y-1),N-y-1,N-x-d1+1 )
        #     # for d2 in range(1,min(N-x-d1,N-y-d1+1)):
        #     for d2 in range(1,min(N-x-d1,N-y-d1+1)):
        #         # x,y에서 d1 만큼 좌하단, d2만큼 우하단, d1만큼 우상단, d2만큼 좌상단 이동 
        #         top =(x,y)
        #         left = (x+d1,y-d1)
        #         bottom = (x+d1+d2,y-d1+d2)
        #         right = (x+d2,y+d2)

        #         print(x,y,d1,d2,'-------------------')
        #         print(top,left,bottom,right,N-x-d1,N-y-d1)
        #         for r in range(N):
        #             for c in range(N):
        #                 if 0 <= r <left[0] and 0<=c<=top[1]:
        #                     check[r][c] = 1
        #                 elif 0<= r <= right[0] and top[1] < c <N:
        #                     check[r][c] = 2
        #                 elif left[0]<= r <N and 0<= c < bottom[1]:
        #                     check[r][c] = 3
        #                 elif right[0]< r < N and bottom[1]<= c < N : 
        #                     check[r][c] = 4
        #         # print(check[x][y],check[x+d1][y-d1],check[x+d1+d2][y-d1+d2], check[x+d2][y+d2] )
        #         check[x][y] = 5
        #         check[x+d1][y-d1]=5
        #         check[x+d1+d2][y-d1+d2]=5
        #         check[x+d2][y+d2] =5


        #         pp(check)



# def paint(x,y,d1,d2):
    




# 기준점 x,y 
def solve(x,y):
    # return 넓이차 
    pass