import sys 
sys.stdin = open('BOJ17182.txt','r')

N,K = map(int,input().split())
time = [[*map(int,input().split())] for _ in range(N)]

print(N,K)
print(time)
