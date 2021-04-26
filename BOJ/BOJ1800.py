# BOJ1800 인터넷 설치 
import sys
sys.stdin = open('BOJ1800.txt','r')

N,P,K = map(int,input().split())
for _ in range(P):
    A,B,price = map(int,input().split())
    