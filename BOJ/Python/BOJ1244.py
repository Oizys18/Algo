import sys
sys.stdin = open('BOJ1244.txt','r')
from pprint import pprint as pp

M = int(input())
lights = [*map(int,input().split())]
N = int(input())
students = [[*map(int,input().split())] for _ in range(N)]

def switch(n):
    if lights[n]:
        lights[n] = 0
    else:
        lights[n] = 1

def solve(student):
    # 남성
    if student[0] == 1:
        for i in range(1,M+1):
            if not i%student[1]:
                switch(i-1)

    # 여성
    elif student[0] == 2:
        match = 0
        for _ in range(M//2+1):
            if student[1]-match < 1 or student[1]+match > M:
                break
            if match == 0:
                switch(student[1]-1)
            elif lights[student[1]-match-1] == lights[student[1]+match-1]:
                switch(student[1]-match-1)    
                switch(student[1]+match-1)    
            else:
                break
            match += 1



for student in students:
    solve(student)
for l in range(1,M+1):
    if not l%20:
        print(lights[l-1])
    else:
        print(lights[l-1],end=' ')