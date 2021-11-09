#  네이버 1차 면접
N = 12345678

# def checkMod(N):
#     number = N
#     N = str(N)
#     for w in N:
#         if number % int(w) != 0:
#             return False
#     return True


# print(checkMod(127))

# def comma(N):
#     cnt = 0
#     ans = ''
#     while N:
#         res = N % 1000
#         N = N // 1000
#         if cnt == 0:
#             ans = str(res) + ans
#         else:
#             ans = str(res) + ',' + ans
#         cnt += 1
#     return ans


def comma(N):
    cnt = 1
    ans = ''
    while N:
        res = N % 10
        N = N // 10
        ans += str(res)
        if cnt % 3 == 0 and cnt:
            ans += ','
        cnt += 1
    return ans[::-1]


print(comma(N))
