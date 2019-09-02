def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    sum = 0
    for i in range(1, 11):
        if a[i] == True:
            sum += i
    if sum == 10:
        for i in range(1, 11):
            if a[i] == True:
                print(i, end = ' ')
        print()

def backtrack(a, k, input):
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 10)


# def backtrack(a, k, sum):
#     global cnt
#     cnt += 1
#     if k == N:
#         if sum == 10:
#             for i in range(1, 11):
#                 if a[i] == True:
#                     print(i, end=' ')
#             print()
#     else:
#         k += 1
#         # if sum + k <= 10 :
#         #     a[k] = 1; backtrack(a, k, sum + k)
# 
#         a[k] = 1; backtrack(a, k, sum + k)
#         a[k] = 0; backtrack(a, k, sum)
# 
# N = 10
# a = [0] * (N + 1)
# 
# cnt = 0
# backtrack(a, 0, 0)
# print("cnt : ", cnt)