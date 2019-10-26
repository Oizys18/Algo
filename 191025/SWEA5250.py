import sys
sys.stdin=open('5250.txt','r')


for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*(N) for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] 


    def isMap(x,y):
        if 0 <= x <= (N+1) and 0 <= y <= (N+1):
            if visit[x][y]:
                return False
            else:
                return True
        else:
            return False

    def BFS(depth,x,y):
        queue = []
        queue.append((depth,x,y))
        while queue:
            depth, x,y = queue.pop(0)
            if not visit[x][y]:
                visit[x][y] = 1
                for i in range(4):
                    newX = x + dx[i]
                    newY = y + dy[i]
                    if isMap(newX,newY):
                        queue.append((depth+1,newX,newY))
        
    BFS(0,0,0)
    
