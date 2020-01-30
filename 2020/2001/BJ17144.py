# 바이바이 미세먼지

R,C,T = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(R)]
cleaner = []
dust = {}
for x in range(R):
    for y in range(C):
        if mat[x][y]:
            if mat[x][y] == -1:
                cleaner.append((x,y))
            elif mat[x][y]:
                dust[(x,y)] = mat[x][y]

def isMap(x,y):
    if 0 <= x < R and 0 <= y < C:
        return True
    else:
        return False

def addDust():
    global dust

    pass

def workCleaner():
    global cleaner
    
    pass

def timeLapse(time):
    time -= 1
    addDust()
    workCleaner()


    if time == 0:
        # return resDust 
        pass   



    