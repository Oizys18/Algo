import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ9874.txt', 'r')

N = int(input())
holes = [[*map(int,input().split())] for _ in range(N)]

holes.sort() # 와 ㅋㅋㅋ 이거 하나 때문에 너무 오래 실수함 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 치사하다 치사해 

def get_hole(hole):
    x,y = holes[hole]
    for i in range(N):
        a,b = holes[i]
        if y == b and a > x:
            return i
    return False 

def check(paired,hole):
        visit = [0]*N
        while True:
            if visit[hole]: return True 
            visit[hole] = True 
            hole = get_hole(hole)
            if not hole:
                return False    
            hole = paired[hole]
            
answer= 0
def pair(k,visit,paired,connected):
    global answer
    if connected == N:
        for i in range(N):
            if check(paired,i):
                answer += 1
                return True
        return 0 
                
    for i in range(k,N):
        if visit[i]:continue 
        visit[i] = 1 
        for j in range(i+1,N): 
            if visit[j]:continue 
            visit[j] = 1 
            paired[i],paired[j] = j, i
            pair(i+1,visit,paired,connected+2)
            paired.pop(i)
            paired.pop(j)
            visit[j] = 0 
        visit[i] = 0
    return 0


pair(0,[0]*N,dict(),0)
print(answer)

# 1 2 3 4 5 6 
# 12 34 56
# 12 35 46 
# 12 36 45 
# 13 24 56
# 13 25 46 
# 13 26 45 
# 14 23 56
# 14 25 36
# 14 26 35  
# 15 23 46
# 15 24 36
# 15 26 34 
# 16 23 45 
# 16 24 35
# 16 25 34  






