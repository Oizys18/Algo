# SWEA1210 Ladder1

import sys
sys.stdin = open('input.txt','r')

# 이진 행렬 Matrix 그리기 
# 마지막 줄에서 2가 있는 곳 좌표값 찾기 : (도착)시작점
# 2가 있는 곳에서 움직이기 시작 
# 이동 함수 def Move()
# 결과값 return, 시작점 도착지점 저장 
# 출력


# def move : 
"""
1. 2의 좌표(시작점)에서 출발
# ( 상이 없을 때까지)반복 
2. 좌/우/상을 살핀다. (하는 없다!)
3-1. 좌/우가 있다면 그쪽으로 이동 
    3-1-1. 만약 길이 계속된다면 이전 이동방향으로 한번 더 이동
    3-1-2. 만약 길이 없다면(다음이 0이라면), 상 으로 한 칸 이동 
3-2. 좌/우가 없고 상만 있다면 상으로 한 칸 이동 
#

-> 도착했다면(천장도착) x 좌표값 출력
"""


# 내 코드 
"""
def Move(mat):
    r = 99
    c = mat[99].index('2')
    direction = 0 # 1: 왼쪽 2: 오른쪽
    while True:
        if direction == 0:
        # 꼭대기 도달 
            if r == 0:
                return c
            # 왼쪽 가장자리  
            elif c == 0:
                if mat[r][c+1] == '1':
                    direction = 2
                    c += 1 
                else:
                    r -= 1
                    direction = 0
            # 오른쪽 가장자리 
            elif c == 99:
                if mat[r][c-1] == '1':
                    direction = 1
                    c -= 1 
                else:
                    r -= 1
                    direction = 0
            # 그냥 중간 
            else:
                # 좌가 '1'
                if mat[r][c-1] == '1':
                    c -= 1
                    direction = 1
                # 우가 '1'    
                elif  mat[r][c+1] == '1':
                    c += 1
                    direction = 2
                # 위만 '1'
                else:
                    r -= 1
                    direction = 0  
        else: 
            if direction == 1:
                if c == 0:
                    r -= 1
                    direction = 0
                elif mat[r][c-1] == '1':
                    c -= 1
                else:
                    direction = 0
                    r -= 1
            elif direction == 2:
                if c == 99:
                    r -= 1
                    direction = 0
                elif mat[r][c+1] == '1':
                    c += 1
                else:
                    direction = 0
                    r -= 1

for T in range(1,11):
    result = 0
    input()
    mat = []
    for _ in range(100):
        mat.append(input().split())
    print("#{0} {1}".format(T,Move(mat)))

"""

"""
right: (0, 1)
left: (0, -1)
up: (-1, 0)

좌표 : (r, c)

가로선 확인
def isHor():
    if mat[r][c+1] == '1' or mat[r][c-1] == '1':


def isWall():
    #벽: return True


    #통로: return False

def right():
    c += 1
def left():
    c -= 1
def up():
    r -= 1


"""




for T in range(1,11):
    input()
    mat = [input().split() for _ in range(100)]
    y = 99
    x = mat[y].index('2')
    while y:
        #우
        if x < 99 and mat[y][x+1] == '1':
            while x < 99 and mat[y][x+1] == '1':
                x += 1
        elif x > 0 and mat[y][x-1] == '1':
            while x > 0 and mat[y][x-1] == '1':
                x -= 1
        y -= 1
    print("#{0} {1}".format(T, x))




