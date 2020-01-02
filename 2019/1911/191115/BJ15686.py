from pprint import pprint as pp
def howfar(cx, cy, hx, hy):
    return abs(cx-hx) + abs(cy-hy)

def comb(k, s):
    global result
    if k == M:
        # tempMat = [[0]*N for _ in range(N)]
        # for cx,cy in temp:
        #     tempMat[cx][cy] = 2
        res = 0
        for hx,hy in dic[1]:
            dis = 10000
            for cx,cy in temp:
                thisChicken = howfar(cx,cy,hx,hy)
                if dis > thisChicken:
                    dis = thisChicken
            res += dis
        if res < result:
            result = res
    else:
        for i in range(s,len(dic[2])-M+k+1):
            temp[k] = dic[2][i]
            comb(k+1, i+1)

N, M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
dic = {
    1:[],
    2:[],
}
for x in range(N):
    for y in range(N):
        if mat[x][y] == 1:
            dic[1].append((x,y))
        elif mat[x][y] == 2:
            dic[2].append((x,y))

result = 1e9
temp = [0]*M
comb(0,0)
print(result)