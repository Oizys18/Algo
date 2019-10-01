# def perm_i():
#     for i1 in range(1, 4):
#         for i2 in range(1, 4):
#             if i2 != i1:
#                 for i3 in range(1, 4):
#                     if i3 != i1 and i3 != i2:
#                         print(i1, i2, i3)


# def perm_r_1(n, r):
#     if r == 0:
#         print(t)
#     else:
#         for i in range(n - 1, -1, -1):
#             # print('arr')
#             # print(arr[:3])
#             arr[i], arr[n - 1] = arr[n - 1], arr[i]
#             # print(arr[i], arr[n - 1])
#             t[r - 1] = arr[n - 1]
#             # print('t')
#             # print(t)
#             perm_r_1(n - 1, r - 1)
#             arr[i], arr[n - 1] = arr[n - 1], arr[i]



# def my_perm(n,r):
#     if r == 0:
#         print(t)
#     else:
#         for i in range(n-1, -1, -1):
#             arr[i], arr[n-1] = arr[n-1], arr[i]
#             t[r-1] = arr[n-1]
#             my_perm(n-1,r-1)
#             arr[i], arr[n-1] = arr[n-1], arr[i]



def perm_r_2(k):
    if k == R:
        print(arr[0], arr[1], arr[2], arr[3])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_2(k + 1)
            arr[k], arr[i] = arr[i], arr[k]




            

"""
k = 0 
N = 3
R = 3 

i  = 0,1,2,3
0 0
i = 0
perm(1)
    i = 1,2,3
    i = 1
    1 1
    1234
        perm(2)
            i = 2,3
            i = 2
            2 2
            1234
                perm(3)
                k = R
                    print(arr = 1,2,3,4)
            1234
            i = 3
            2 3
            1243
                perm(3)
                k = R
                    print(arr = 1,2,4,3)
            1234
        1234
    i = 2
    2 1
    1324
        perm(2)
            i = 2,3
            i = 2
            2 2
            1324
                perm(3)
                k = R
                    print(arr = 1,3,2,4)
            1324

            i = 3
            2 3
            1342
                perm(3)
                k = R
                    print(arr = 1,3,4,2)
            1324
        1234
    i = 3
    1 3
    1432
        perm(2)
            i = 2,3
            i = 2
            2 2
            1432
                perm(3)
                k = R
                    print(1432)
                1432
            i = 3
            2 3
            1423
                peirn(1423)
            1432
        1234
1234
i = 1
0 1
2134
    perm(1)
    i = 1,2,3
    i = 1
    1 1 




            




"""




# def perm_r_3(k):
#     if k == N:
#         print(t)
#     else:
#         for i in range(N):
#             if visited[i]: continue
#             t[k] = arr[i]
#             visited[i] = 1
#             perm_r_3(k + 1)
#             visited[i] = 0



# print('순열 반복문')
# perm_i()

N = 4
R = 4
# a = [0] * N
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# t = [0] * N
# print('순열 재귀문1')
# perm_r_1(N, R)


print('순열 재귀문2')
perm_r_2(0)


# visited = [0] * N
# print('순열 재귀문3')
# perm_r_3(0)
