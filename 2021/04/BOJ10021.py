import sys
sys.stdin = open('BOJ10021.txt','r')

N,C = map(int,input().split(' '))
data = {i:tuple(map(int,input().split(' '))) for i in range(N)}
print(N,C)
print(data)