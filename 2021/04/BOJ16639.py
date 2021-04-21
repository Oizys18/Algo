import sys 
sys.stdin=open('BOJ16639.txt','r')

def getMinMax(line,i):
    b = line[-2:]
    mn,mx = dp[i-1]
    mnb = eval(str(mn) + b)
    mxb = eval(str(mx) + b)
    dp[i] = (min(mnb,mxb),max(mnb,mxb))
    return

# for _ in range(6): # tc 갯수
N = int(input())
line = input()
dp = {}

f = eval(str(eval(line[0:3])) + line[3:5])
b = eval(line[0:2] + str(eval(line[2:5])))
dp[0] = (min(f,b),max(f,b))

for i in range(1,N//2-1):
    getMinMax(line[0:5+2*i],i)
print(dp[i][1])


