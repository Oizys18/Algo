'==================== 반복문 ========================='


def comb_i():
    for i in range(N - 1):
        for j in range(i + 1, N):
            print(a[i], a[j])


def pi_i():
    for i in range(N):
        for j in range(N):
            print(a[i], a[j])


def H_i():
    for i in range(N):
        for j in range(i, N):
            print(a[i], a[j])


'=================== 조합 ============================'


def comb_r_1(n, r):
    if r == 0: print(t[0], t[1])
    elif n < r: return
    else:
        t[r - 1] = a[n - 1]
        comb_r_1(n - 1, r - 1)
        comb_r_1(n - 1, r)


def comb_r_2(k, s):
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r_2(k + 1, i + 1)


'===================== 중복 순열 ========================='


def pi_r_1(n, r):
    if r == 0: print(t[0], t[1])
    else:
        for i in range(n - 1, -1, -1):
            a[i], a[n - 1] = a[n - 1], a[i]
            t[r - 1] = a[n - 1]
            pi_r_1(n, r - 1)
            a[i], a[n - 1] = a[n - 1], a[i]


def pi_r_2(k):
    if k == R: print(t[0], t[1])
    else:
        for i in range(N):
            t[k] = a[i]
            pi_r_2(k + 1)


'====================== 중복 조합 ========================'


def H_r_1(n, r):
    if r == 0: print(t[0], t[1])
    elif n == 0: return     ####### 주의!!!
    else:
        t[r - 1] = a[n - 1]
        H_r_1(n, r - 1)
        H_r_1(n - 1, r)


def H_r_2(k, s):
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N):
            t[k] = a[i]
            H_r_2(k + 1, i)


'=================================================='

N = 3
R = 2
a = [1, 2, 3]
t = [0] * R

print('조합')
comb_i()
print("----------")
comb_r_1(N, R)
print("----------")
comb_r_2(0, 0)

print()
print("중복 순열")
pi_i()
print("----------")
pi_r_1(N, R)
print("----------")
pi_r_2(0)

print()
print("중복 조합")
H_i()
print("----------")
H_r_1(N, R)
print("----------")
H_r_2(0, 0)
