# 감시피하기
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ18428.txt', 'r')

N = int(input())

mat = [[*input().split()] for _ in range(N)]

pp(mat)

pp(list(map(list,zip(*mat))))