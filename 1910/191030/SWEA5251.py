import sys
sys.stdin = open('5251.txt', 'r')

for T in range(int(input())):
    N, E = map(int,input().split())
    for i in range(E):
        s, e, w = map(int,input().split())
         