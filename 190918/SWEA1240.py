#SWEA1240 단순2진암호

import sys 
from pprint import pprint as pp
sys.stdin = open('input.txt','r')

def decom(n):
    if n == '0001101':
        return 0
    elif n == '0011001':
        return 1
    elif n == '0010011':
        return 2
    elif n == '0111101':
        return 3
    elif n == '0100011':
        return 4
    elif n == '0110001':
        return 5
    elif n == '0101111':
        return 6
    elif n == '0111011':
        return 7
    elif n == '0110111':
        return 8
    elif n == '0001011':
        return 9



for T in range(int(input())):
    N, M = map(int,input().split())
    pw = []
    for _ in range(N):
        line = input().strip('0')
        if pw:
            continue
        else:
            if line:
                lineL = len(line)
                if lineL < 56 : 
                    pw = (56 - lineL)*'0' + line

    odd = []
    even = []
    for j in range(8):
        if j == 7:
            vrf = decom(pw[0+7*j:7+7*j])
        elif j % 2 == 0:
            odd.append(decom(pw[0+7*j:7+7*j]))
        elif j % 2 != 0:
            even.append(decom(pw[0+7*j:7+7*j]))

    res = (sum(odd)*3) + sum(even) + vrf
    if res % 10 == 0:
        print("#{} {}".format(T+1, sum(odd) + sum(even) + vrf))
    else:
        print("#{} {}".format(T+1,0))
