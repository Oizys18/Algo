T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    honeyPot = [[0]*N for _ in range(N)]
 
    for row in range(N):
        for col in range(N-M+1):
            bee = honey[row][col:col+M]
            if sum(bee) > C:
                temp_sum = 0
                """
                넘모 넘모 신기한 부분집합 코드입니다~~~~~
                넘모 신기해 ~~~~ 
                """
                powerset = [[]]
                for b in bee:
                    temp = [x + [b] for x in powerset]
                    powerset += temp
                """
                최솔지님의 코드 입니다 
                soulg_choi 
                """
                for p in powerset:
                    if sum(p) <= C:
                        sum_p = 0
                        for pp in p:
                            sum_p += pp ** 2
                        if temp_sum < sum_p:
                            temp_sum = sum_p
                            bee = p
            for e in bee:
                honeyPot[row][col] += e**2
        sum_honey = (0, 0)
        for col2 in range(N-M+1):
            if honeyPot[row][col2] > sum_honey[0]:
                sum_honey = honeyPot[row][col2], col2
        for i in range(sum_honey[1]-M+1, sum_honey[1]+M):
            honeyPot[row][i] = 0
        honeyPot[row][sum_honey[1]] = sum_honey[0]
 
    honeyPot2 = sorted(sum(honeyPot, []), reverse=True)
    print('#%d %d' % (tc, honeyPot2[0] + honeyPot2[1]))