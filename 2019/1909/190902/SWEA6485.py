import sys
sys.stdin = open('input2.txt','r')

for T in range(int(input())):
    N = int(input())
    stop = []    
    for n in range(N):
        a,b = map(int,input().split())
        stop.append((a,b))
    P = int(input())
    stops = [0]*(5000)
    for bus in stop:
        a,b = bus
        for k in range(b-a+1):
            stops[a+k-1] += 1
    print("#{0}".format(T+1),end=' ')
    for p in range(P):
        print(stops[int(input())-1],end=' ')
    print()