for tc in range(T):
    n, m, k = map(int, input().split())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))
    max = li[0][0]
    for r in range(n-k+1):
        for c in range(m-k+1):
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
            idx = 0
            mysum = 0
            for nn in range(k*4-4):
                mysum += li[r][c]
                r += dr[idx]
                c += dc[idx]
                if nn % (k-1) == 0 and nn > 0:
                    r -= dr[idx]
                    c -= dc[idx]
                    idx = (idx + 1) % 4
                    r += dr[idx]
                    c += dc[idx]
            if max < mysum:
                max = mysum
    print('#{} {}'.format(tc+1, max))