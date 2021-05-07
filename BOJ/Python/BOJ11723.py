# 집합
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ11723.txt', 'r')
M = int(input())
S = [0]*21
for _ in range(M):
    work = sys.stdin.readline()
    if work == 'all\n' or work=='empty\n':
        what = work
    else:
        what,num = work.split()
        num = int(num)
    if what == 'add':
        if not S[num]:S[num] = 1 
    elif what == 'remove':
        if S[num]:S[num] = 0
    elif what == 'check':
        if S[num]:print(1)
        else: print(0)   
    elif what == 'toggle':
        S[num] = not S[num] 
    elif what == 'all\n':
        S = [1]*21
    elif what == 'empty\n':
        S = [0]*21


"""
9번줄의 'all\n'에 주목. readline()할 때 개행문자도 같이 읽는다. 

1. Pypy에서 메모리초과 실패
2. Python3에서는 통과
3. import sys를 제출할 때 빼먹어서 NameError나는 걸 놓쳐서 여러번 Fail함 

"""