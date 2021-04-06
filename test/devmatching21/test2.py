rows =3
columns = 3
queries = 	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
from pprint import pprint as pp

def solution(rows, columns, queries):
    answer = []
    # right , down, left, up
    direc = [0,1,2,3]
    mat = [[0]*columns for _ in range(rows)]
    n = 1 
    for x in range(rows):
        for y in range(columns):
            mat[x][y] = n
            n+=1

    def isWall(x,y,left,right,up,down):
        if left<= x <= right:
            if up <= y <= down:
                return True
        return False
    
    def next_move(x,y,direc):
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        if direc == 0:
            return (x+direction[0][0],y+direction[0][1])
        elif direc == 1:
            return (x+direction[1][0],y+direction[1][1])
        elif direc == 2:
            return (x+direction[2][0],y+direction[2][1])
        elif direc == 3:
            return (x+direction[3][0],y+direction[3][1])
    
    def turn(query):
        x1,y1,x2,y2 = query
        length = (x2-x1+1)*2 + (y2-y1+1)*2 - 4
        x,y = x1,y1
        start = mat[x][y-1]
        cur = mat[x-1][y-1] 
        direc = 0
        minNum = 100000
        for i in range(length):
            if i == length:
                mat[x-1][y-1] = start
                break
            else:
                nx,ny = next_move(x,y,direc)    
                if not isWall(nx,ny,x1,x2,y1,y2):
                    direc += 1 
                    nx,ny = next_move(x,y,direc)
                nxt = mat[nx-1][ny-1]
                mat[nx-1][ny-1] = cur
                cur = nxt
                x,y = nx,ny
            if mat[x-1][y-1] <= minNum:
                minNum = mat[x-1][y-1]
        return minNum
    

    for j in range(len(queries)):
        answer.append(turn(queries[j]))

    return answer
print(solution(rows,columns,queries))