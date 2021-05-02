import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1003.txt', 'r')

def fibo(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1 
    else:
        return temp[N-2] + temp[N-1]

temp = [0]*41

for i in range(41):
    temp[i] = fibo(i)

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(f"{1} {0}")
    elif N == 1:
        print(f"{0} {1}")
    else:
        print(f"{temp[N-2]} {temp[N-1]}")


