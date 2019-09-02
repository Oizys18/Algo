# SWEA5097
"""
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 
수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
"""
import sys
sys.stdin = open('input2.txt','r')

for T in range(int(input())):
    N,M = map(int,input().split())
    line = list(map(int,input().split()))
    idx = M % N
    print("#{0} {1}".format(T+1,line[idx]))     