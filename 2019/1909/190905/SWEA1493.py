# SWEA 1493
import sys
from pprint import pprint

sys.stdin = open('input4.txt','r')
def dot(num):
    n = 1
    while True:
        edge = (n * (n+1))//2
        if num <= edge:
            return (n-(edge-num),1+(edge-num))
        n += 1
        
def dot2(x,y):
    return ((((x+y-2) * (x+y-1))//2) +1) + x-1

for T in range(int(input())):
    p, q = map(int,input().split()) 
    P, Q = dot(p), dot(q)
    print("#{} {}".format(T+1,dot2(P[0]+Q[0], P[1]+Q[1])))








"""
x,y 

x,y: (((x+y-2) * (x+y-1))//2) +1

2:1~1 (1)1,1  
3:2~3 (2)1,2 2,1  
4:4~6 (4 = 2+2)1,3 2,2 1,3        
5:7~10 (7 = 2+2+3)1,4 2,3 3,2 4,1   
6:11~15 (11 = 2+2+3+4)1,5 2,4 3,3 4,2 5,1 
7:16~21 (16 = 2+2+3+4+5)
8:22~28 (22) 27 : 54 
9:29~36 (29)
10:37~45 (37) 

3,2? 
-> 1,4 2,3 3,2 4,1 
7      8    9 
...
x+y-2: ()1,x+y-3
x+y-1: (a)1,x+y-2
x+y: [{1 ~ (x+y+2)-2} + 1 ]    ///  1,x+y-1, .......... x+y-1,1 
n : (1~n-2) + 1        


p,q: 
-> 1,p+q-1 ~ p+q-1,1  포함 
"""

    
