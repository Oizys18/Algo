import sys 
sys.stdin=open('BOJ16639.txt','r')
from pprint import pprint as pp 

def calc(a,what,c):
    if what =='+':
        return a+c
    elif what =='-':
        return a-c
    else:
        return a*c

N = int(input())
line = input()
mx = [[0]*N for _ in range(N)]
mn = [[0]*N for _ in range(N)]

for i in range(0,N-2,2):
    mx[i][i],mx[i+2][i+2] = int(line[i]),int(line[i+2])
    mn[i][i],mn[i+2][i+2] = int(line[i]),int(line[i+2])
    mx[i][i+2] = calc(int(line[i]),line[i+1],int(line[i+2]))
    mn[i][i+2] = calc(int(line[i]),line[i+1],int(line[i+2]))
print("LINE",line)
for i in range(4,N,2):
    for j in range(i,N,2):
        flag = 1
        mmx = 0
        mmn = 0
        print(j-i,j,'=============================',line)
        for k in range(j-i,j,2):
            print(j-i,k,line[k+1],k+2,j)
            t_mxmx = calc(mx[j-i][k],line[k+1],mx[k+2][j])
            t_mxmn = calc(mx[j-i][k],line[k+1],mn[k+2][j])
            t_mnmx = calc(mn[j-i][k],line[k+1],mx[k+2][j])
            t_mnmn = calc(mn[j-i][k],line[k+1],mn[k+2][j])
            print("t_mxmx,t_mxmn,t_mnmx,t_mnmn:",t_mxmx,t_mxmn,t_mnmx,t_mnmn)
            tmax = max(t_mxmx,t_mxmn,t_mnmx,t_mnmn)
            tmin = min(t_mxmx,t_mxmn,t_mnmx,t_mnmn)
            if flag:
                mmx = tmax
                mmn = tmin
                flag = 0
            else:
                if mmx < tmax:
                    mmx = tmax
                if mmn > tmin:
                    mmn = tmin
        mx[j-i][j] = mmx
        mn[j-i][j] = mmn
        print(mmx,mmn)
print(mx[0][N-1])

pp(mx)
pp(mn)

"""
왜 틀리는지 이해 못하겠음; ㅠ 
"""