# '==================== 라이브러리 순열, 중복순열, 조합, 중복조합 ========================='
# # from itertools import permutations
# # per = permutations([1,2,3],2)
# # print(list(per))
# # #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# # from itertools import product
# # per = product([1,2,3],repeat=2)
# # print(list(per))
# # #[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# from itertools import combinations
# print(list(combinations([1,2,3],2) ) )
# #[(1, 2), (1, 3), (2, 3)]

# # from itertools import combinations_with_replacement
# # print( list ( combinations_with_replacement([1,2,3],2) ) )
# # #[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


# print('--------------------------------------------------------')

# '==================== 조합 ========================='


# def comb_i():
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             print(a[i], a[j])

# '''
# 1 2
# 1 3
# 2 3
# '''

def comb_r(k, s):
    if k == R: print(t)
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)

'''
1 2
1 3
2 3

'''


# '===================== 중복 순열 ========================='

# def pi_i():
#     for i in range(N):
#         for j in range(N):
#             print(a[i], a[j])

# '''
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# '''

# def pi_r(k):
#     if k == R: print(t[0], t[1])
#     else:
#         for i in range(N):
#             t[k] = a[i]
#             pi_r(k + 1)

# '''
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# '''


# '====================== 중복 조합 ========================'

# def H_i():
#     for i in range(N):
#         for j in range(i, N):
#             print(a[i], a[j])

# '''
# 1 1
# 1 2
# 1 3
# 2 2
# 2 3
# 3 3
# '''

# def H_r(k, s):
#     if k == R: print(t[0], t[1])
#     else:
#         for i in range(s, N):
#             t[k] = a[i]
#             H_r(k + 1, i)
# '''
# 1 1
# 1 2
# 1 3
# 2 2
# 2 3
# 3 3
# '''

'====================== 호출 ========================'
N = 3
R = 2
a = [1, 2, 3]
t = [0] * R




# print()
# print('조합')
# comb_i()
print("----------")
comb_r(0, 0)

# print()
# print("중복 순열")
# pi_i()
# print("----------")
# pi_r(0)

# print()
# print("중복 조합")
# H_i()
# print("----------")
# H_r(0, 0)

