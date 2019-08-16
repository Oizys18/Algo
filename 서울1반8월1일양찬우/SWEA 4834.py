# SWEA 4834. 숫자카드

for case in range(int(input())):
    counts = [0] * 10
    N = int(input())
    cards = [int(c) for c in input()]

    for i in range(10):
        # 카드 갯수 count
        for card in cards:
            if i == card:
                counts[i] += 1

    freq_card = 0
    for a in range(10):
        if counts[a] >= counts[freq_card]:
            freq_card = a

    print("#{0} {1} {2}".format(case+1,freq_card,counts[freq_card]))
