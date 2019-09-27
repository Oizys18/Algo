
def perm_i():
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2, i3)


def perm_r_1(n, r):
    if r == 0:
        print(t[0], t[1], t[2])
    else:
        for i in range(n - 1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            t[r - 1] = arr[n - 1]
            perm_r_1(n - 1, r - 1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


def perm_r_2(k):
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_2(k + 1)
            arr[k], arr[i] = arr[i], arr[k]



def perm_r_3(k):
    if k == N:
        print(t[0], t[1], t[2])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm_r_3(k + 1)
            visited[i] = 0



print('순열 반복문')
perm_i()

N = 3
R = 3

a = [0] * N
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t = [0] * N
print('순열 재귀문1')
perm_r_1(N, R)


print('순열 재귀문2')
perm_r_2(0)


visited = [0] * N
print('순열 재귀문3')
perm_r_3(0)
