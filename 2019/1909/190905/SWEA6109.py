# SWEA6109 

import sys
from pprint import pprint
sys.stdin = open('input.txt','r')
"""
stack 이용 풀어보자 

1. 빈 스택에 처음으로 들어갈 숫자를 push
2. 다음으로 들어올 숫자를 스택의 top과 비교
 2-1 같다면 stack.pop()한 값을 *2 해서 다시 push, 'new'push (구분벽)
 2-2 다르다면 그냥 push 
3. stack에서 하나씩 빼낸 다음 밀어낸 쪽의 끝부터 하나씩 삽입
4. 출력 기준에 맞게 출력 
"""

def stack(line,dr):
    stack = []
    if dr == 'right' or dr == 'down':
        temp = list(reversed(line))
    elif dr == 'left' or dr == 'up':
        temp = list(line)

    stack.append('s')
    while temp:
        num = temp.pop(0)
        if num == 0:
            continue
        elif num == stack[-1]:
            stack.append(stack.pop() * 2)
            stack.append('p')
        elif num != stack[-1]:
            stack.append(num)
    res = []
    for i in stack:
        if i == 's' or i == 'p':
            continue
        else:
            res.append(i)
    return res
        
for T in range(int(input())):
    N, S = input().split()
    N = int(N)
    S = str(S)
    mat = [list(map(int,input().split())) for _ in range(N)]
    rmat = list(zip(*mat))
    resMat = []
    # 열 계산 zip 사용
    if S == 'up' or S == 'down':
        for x in range(N):
            res = stack(rmat[x],S)
            if S == 'up':
                res.extend([0]*(N-len(res)))
                resMat.append(res)
            elif S == 'down':
                res = [0]*(N-len(res)) + list(reversed(res))
                resMat.append(res)
        resMat = list(zip(*resMat))

    elif S == 'right' or S == 'left':
        for x in range(N):
            res = stack(mat[x],S)
            if S == 'right':
                res = [0]*(N-len(res)) + list(reversed(res))
                resMat.append(res)
            elif S == 'left':
                res.extend((N-len(res))*[0])
                resMat.append(res)

    print("#{}".format(T+1))
    for x in range(N):
        for y in range(N):
            print(resMat[x][y],end=' ')
        print()


    