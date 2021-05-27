# Hard Choice
import sys
sys.stdin = open('BOJ15059.txt','r')
from pprint import pprint as pp


A,B,C = map(int,input().split())
AA,BB,CC = map(int,input().split())

cnt = 0 
if AA > A: 
    cnt += AA-A
if BB > B:
    cnt += BB-B
if CC > C:
    cnt += CC-C 
print(cnt)