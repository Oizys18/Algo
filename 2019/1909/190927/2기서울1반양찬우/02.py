import sys
import itertools
sys.stdin=open('input.txt','r')
for T in range(int(input())):
    input()
    mat = [list(map(int,input().split())) for _ in range(10)]
    robot = []
    cookie = []
    robotCookie = {1:0,2:0,3:0,4:0,5:0,6:0}
    for x in range(10):
        for y in range(10):
            if 0 < mat[x][y] < 7:
                cookie.append((x, y))
            elif mat[x][y] == 9:
                robot.append((x,y))

    cookieFar = {1:[0]*6,2:[0]*6,3:[0]*6,4:[0]*6,5:[0]*6,6:[0]*6}
    for r in range(6):
        x,y = robot[r]
        for c in range(6):
            a,b = cookie[c]
            vert = abs(max(a,x) - min(a,x))
            hori = abs(max(b,y) - min(b,y))
            cookieFar[r+1][c]= vert+hori
    result = 0
    finalRes = 5000
    for choice in itertools.permutations(range(6),6):
        for cho in range(6):
            result += cookieFar[cho + 1][choice[cho]]
        if result < finalRes:
            finalRes = result
        result = 0
    print("#{} {}".format(T+1,finalRes))
