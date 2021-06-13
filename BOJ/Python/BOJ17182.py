import sys 
sys.stdin = open('BOJ17182.txt','r')

# 탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.

# 행성갯수, 행성위치
N,K = map(int,input().split())
time = [[*map(int,input().split())] for _ in range(N)]
def travel(now,total): 



travel(K,0)
print(N,K)
print(time)
