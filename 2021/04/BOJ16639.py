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
mx = [[-sys.maxsize]*N for _ in range(N)]
mn = [[sys.maxsize]*N for _ in range(N)]

for i in range(0,N):
    if line[i].isnumeric():
        mx[i][i] = mn[i][i] = int(line[i]) 
for j in range(0,N-2,2):
    mx[j][j+2] = calc(int(line[j]),line[j+1],int(line[j+2]))
    mn[j][j+2] = calc(int(line[j]),line[j+1],int(line[j+2]))

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
# for j in range(2,N,2):
#     for i in range(0,N-j,2):
#         for k in range(2,j+1,2):
#             print("i,i+k-2,i+k-1,i+k,i+j:",i,i+k-2,i+k-1,i+k,i+j)
#             temp = [0]*4
#             temp[0] = calc(mn[i][i + k - 2], line[i + k - 1], mn[i + k][i + j]);
#             temp[1] = calc(mn[i][i + k - 2], line[i + k - 1], mx[i + k][i + j]);
#             temp[2] = calc(mx[i][i + k - 2], line[i + k - 1], mn[i + k][i + j]);
#             temp[3] = calc(mx[i][i + k - 2], line[i + k - 1], mx[i + k][i + j]);

#             temp.sort()

#             mn[i][i + j] = min(temp[0],mn[i][i+j]);
#             mx[i][i + j] = max(temp[3],mx[i][i+j]);

#             print(mn[i][i + j], mx[i][i + j])
print(mx[0][N-1])


"""
왜 틀리는지 이해 못하겠음; ㅠ 
"""
