import sys
sys.stdin = open('input3.txt','r')

# def memo(k, s):
#     if res[k][s]: return
#     res[k][s] = 1
#     if k == N:
#         return
#     else:
#         memo(k + 1, s)
#         memo(k + 1, s + scores[k])
        

# for T in range(int(input())):
#     N = int(input())
#     scores = [*map(int,input().split())]
#     res = [[0]*(sum(scores)+1) for _ in range(N+1)]
#     memo(0, 0)
#     print("#{} {}".format(T+1, sum(res[N])))


TC = int(input())
for testcase in range(1, TC+1):
    N = int(input())
    new_lst = list(map(int, input().split()))
    cnt = 1
    score_ck = [0 for _ in range(N*100)]
    score_lst = [0]
    for i in range(N):
        for j in range(cnt):
            ans = new_lst[i] + score_lst[j]
            if score_ck[ans] == 0:
                score_ck[ans] = 1
                score_lst.append(ans)
                cnt += 1
    print('#{} {}'.format(testcase, cnt))