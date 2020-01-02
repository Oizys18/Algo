# SWEA5108
import sys
sys.stdin = open('input4.txt','r')
for T in range(int(input())):
    N, M, L = map(int,input().split())
    li = list(map(int,input().split()))
    # li.extend([0]*M)
    for m in range(M):
        idx, num = map(int,input().split())
        li.insert(idx,num)
    print("#{0} {1}".format(T+1,li[L]))