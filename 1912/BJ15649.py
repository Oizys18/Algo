import sys
sys.stdin=open("BJ15649.txt",'r')

N, M = map(int,input().split())

def perm(k):
    if k == M:
        return
    else:
