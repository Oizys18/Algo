# 감시피하기
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ18428.txt', 'r')
# 장애물 3개 설치해서 모든 학생 감시 피할 수 있는지 여부 출력 ( YES  or NO)
N = int(input())

mat = [[*input().split()] for _ in range(N)]
# turned = list(map(list,zip(*mat)))
dx = [0,0,-1,1]
dy = [-1,1,0,0]

pp(mat)
students = set()
teachers = set()
for x in range(N):
    for y in range(N):
        if mat[x][y] == 'S':
            students.add((x,y))
        elif mat[x][y] == 'T':
            teachers.add((x,y))
