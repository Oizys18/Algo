# SWEA 4381. 전기버스

cnt = 0
for case in range(int(input())):
    K, N, Ml = list(map(int, (input().split())))
    M = list(map(int, (input().split())))
    # 0에서 시작, 종점 N
    M = [0] + M + [N]
    # 현재위치
    now = 0
    # 정거 횟수
    result = 0
    # 한 정거장을 건너뛰었는가?
    jump = 0
    while now < N:
        now = now + K
        for i in range(len(M)):
            if now >= N:
                break
            else:
                if jump == 0:
                    if now < M[i+1]:
                        result = 0
                        now = N
                    elif now >= M[i+2] and now < M[i+3]:
                        now = M[i+2]
                        result += 1
                        now = now + K
                        jump = 1
                    elif now >= M[i+1] and now < M[i+2]:
                        now = M[i+1]
                        result += 1
                        now = now + K
                else:
                    jump = 0
                    continue

    print("#{0} {1}".format(case+1,result))
