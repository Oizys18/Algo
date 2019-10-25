import sys
sys.stdin=open('5250.txt','r')


for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    print(mat)