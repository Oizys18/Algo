# SWEA 1259 금속막대
import sys
sys.stdin = open('input.txt', 'r')
for case in range(int(input())):
    n = int(input())
    boltNum = list(map(int, input().split()))
    bs = []
    for i in range(n):
        bs.append([boltNum[2*i], boltNum[2*i+1]])
    s_bs = bs[0]

    while True:
        for bt in range(len(bs)):
            if s_bs[len(s_bs)-1] == bs[bt][0]:
                s_bs = s_bs + bs[bt]
            elif s_bs[0] == bs[bt][1]:
                s_bs = bs[bt] + s_bs
        if len(boltNum) == len(s_bs):
            break

    print('#{0}'.format(c + 1), end=' ')
    for j in s_bs:
        print(j, end=' ')
    print('')