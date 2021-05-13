import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1629.txt', 'r')

A,B,C = map(int,input().split())
print(pow(A,B,C))
"""
https://stackoverflow.com/questions/14133806/why-is-powa-d-n-so-much-faster-than-ad-n
https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221137999832&proxyReferer=https:%2F%2Fwww.google.com%2F

pow 함수
- pow(A,B) = A**B 
- pow(A,B,C) = (A**B)%C
"""

