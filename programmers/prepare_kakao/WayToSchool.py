def solution(m, n, puddles):
    mat = [[0]*m for _ in range(n)]
    for puddle in puddles:
        mat[puddle[1]-1][puddle[0]-1] = -1
    mat[0][0] = 1 
    for x in range(n):
        for y in range(m):
            if mat[x][y] == -1 or (x==0 and y==0):
                continue
            else:
                if x != 0:
                    top = max(mat[x-1][y],0)
                else: 
                    top = 0
                if y != 0:
                    left = max(mat[x][y-1],0)   
                else: 
                    left = 0
                mat[x][y] = (top + left) % 1000000007 
    return mat[n-1][m-1]

# 좀 더 정제한 버전
def solution(m, n, puddles):
    mat = [[0]*m for _ in range(n)]
    for puddle in puddles:
        mat[puddle[1]-1][puddle[0]-1] = -1
        
    def isMap(x,y):
        return 0<=x<n and 0<=y<m and mat[x][y]>0
    
    mat[0][0] = 1 
    for x in range(n):
        for y in range(m):
            if mat[x][y] == -1 or (x==0 and y==0):
                continue
            else:
                temp = 0
                if isMap(x-1,y):
                    temp += mat[x-1][y]
                if isMap(x,y-1):
                    temp += mat[x][y-1]
                mat[x][y] = temp %1000000007
    return mat[n-1][m-1]


"""
처음에 x==0 과 y==0, 즉 맨 윗줄과 맨 왼쪽 줄을 1로 설정하고 계산을 시작했는데 자꾸 실패했다.
결국 다른 사람 누군가가 적어놓은 글을 읽고 해결했다. 

생각해보니 처음 시작점을 웅덩이가 모두 가로막고있다면 마지막 m,n은 0이어야하지만, 
내가 한 것처럼 1로 모두 도배해버리면 m,n이 0이 되지 않는다. 

즉, 0,0을 1로 설정한 후, (위,왼쪽)에 타일이 있다면 확인하는 방법으로 계산해야한다. 
"""