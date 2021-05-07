import sys
sys.stdin=open('BOJ2475.txt','r')

print(sum([i**2 for i in map(int,input().split())])%10)