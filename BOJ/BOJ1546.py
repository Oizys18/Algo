import sys
sys.stdin=open('BOJ1546.txt','r')
N = int(input())
numbers = list(map(int,input().split()))
mx_n = max(numbers)
print(sum([i/mx_n*100  for i in numbers])/N)