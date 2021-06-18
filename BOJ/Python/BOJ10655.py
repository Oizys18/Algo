#마라톤 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ10655.txt', 'r')

N = int(input())
mat = [[*map(int,input().split())] for _ in range(N)]

def getLength(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

skipped = 0
total = getLength(mat[0],mat[1]) 
for mid in range(1,N-1):
    gap = getLength(mat[mid-1],mat[mid]) + getLength(mat[mid],mat[mid+1]) - getLength(mat[mid-1],mat[mid+1])
    skipped = max(skipped, gap)
    total += getLength(mat[mid],mat[mid+1])

print(total-skipped)