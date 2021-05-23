# 감시피하기
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ18428.txt', 'r')


# 장애물 3개 설치해서 모든 학생 감시 피할 수 있는지 여부 출력 ( YES  or NO)
# teacher 가 5이하, 학생이 30이하, 빈칸은 3개 이상임 


from itertools import combinations
N = int(input())

mat = [[*input().split()] for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

students = set()
teachers = set()
obstacles = set()

for x in range(N):
    for y in range(N):  
        if mat[x][y] == 'S':
            students.add((x,y))
        elif mat[x][y] == 'T':
            teachers.add((x,y))

def isMap(x,y):
    return 0<=x<N and 0<=y<N

# 감시 확인 함수 
def check():
    caught = []
    for x,y in teachers:
        for sx,sy in students: 
            flag = 0
            if x == sx:
                flag = 1 
                for ox,oy in obstacles:
                    if x == ox and (y < oy < sy or sy < oy < y):
                        flag = 0 # blocked
            elif y == sy:
                flag = 1 
                for ox,oy in obstacles:
                    if y == oy and (x < ox < sx or sx < ox < x) :
                        flag = 0
            if flag:
                caught.append((sx,sy,x,y))
    return caught

caught = check()
obstacle_poss = []

if not caught:
    print('YES')
else:
    for sx,sy,x,y in caught:
        if sx == x:
            for i in range(min(y,sy)+1, max(y,sy)):
                obstacle_poss.append((x,i))
        elif sy == y:
            for j in range(min(x,sx)+1, max(x,sx)):
                obstacle_poss.append((j,y))
    pick = min(3,len(obstacle_poss))
    for comb in combinations(obstacle_poss,pick):
        for x,y in comb:
            obstacles.add((x,y))
        caught = check()
        if not caught:
            print('YES')
            break
        obstacles = set()
    else:
        print('NO')
