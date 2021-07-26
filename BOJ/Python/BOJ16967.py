# 배열복원
import sys
sys.stdin = open('BOJ16967.txt','r')
from pprint import pprint as pp

"""
크기가 H × W인 배열 A와 두 정수 X와 Y가 있을 때, 크기가 (H + X) × (W + Y)인 배열 B는 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만들 수 있다. 수가 겹쳐지면 수가 합쳐진다.

즉, 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.

(i, j)가 두 배열 모두에 포함되지 않으면, Bi,j = 0이다.
(i, j)가 두 배열 모두에 포함되면, Bi,j = Ai,j + Ai-X,j-Y이다.
(i, j)가 두 배열 중 하나에 포함되면, Bi,j = Ai,j 또는 Ai-X,j-Y이다.
배열 B와 정수 X, Y가 주어졌을 때, 배열 A를 구해보자.
"""

H,W,X,Y = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(H+X)]
pp(mat)
pp(H,W,X,Y)

