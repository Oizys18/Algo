import sys 
sys.stdin = open('BOJ17182.txt','r')

# 탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.

# 행성갯수, 행성위치
N,K = map(int,input().split())
time = [[*map(int,input().split())] for _ in range(N)]
MAX = 10000
visit = [0]*N

score = [MAX]*N

def travel(now,total):
    print(now,total)
    score[now] = min(score[now],total)
    if sum(visit) == N:
        print(score)
        print(visit)
        return total 
    else:
        for i in range(N):
            if i != now:
                visit[i] = 1
                return travel(i,total+time[now][i])
                visit[i] = 0

travel(K,0)

"""
플로이드 와샬 문제임 
"""