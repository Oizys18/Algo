# 사칙연산

import sys
sys.stdin=open('input.txt','r')

import math
for T in range(10):
    N = int(input())
    info = [input().split() for _ in range(N)]
    infoli = {}
    for i in range(N):
        if len(info[i]) == 2:
            infoli[int(info[i][0])] = [0,info[i][1],0]
        else:
            infoli[int(info[i][0])] = [int(info[i][2]),info[i][1],int(info[i][3])]

    queue= []
    def solve(node):
        if node > N or node == 0:
            return
        else:
            solve(infoli[node][0]) 
            solve(infoli[node][2])

            if infoli[node][1] not in '+-*/':
                queue.append(infoli[node][1])
            else:
                r = queue.pop()
                l = queue.pop()
                if infoli[node][1] == '+':
                    queue.append(int(l)+int(r))
                elif infoli[node][1] == '-':
                    queue.append(int(l)-int(r))
                elif infoli[node][1] == '*':
                    queue.append(int(l)*int(r))
                elif infoli[node][1] == '/':
                    queue.append(int(l)/int(r))
    solve(1)
    print(f"#{T+1} {math.floor(queue.pop())}")
