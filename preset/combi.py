def comb_r(k, s):
    if k == R: 
        print(t)
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)

N = 3
R = 2
a = [1, 2, 3]
t = [0] * R
comb_r(0, 0)
#재귀 조합





"""
# R = 몇개 선택?
# N = array의 길이 
# t = array의 길이와 같은 빈 리스트 
s = 0, k = 0, R = 3, N = 3 a = [1,2,3], t = [0,0,0]

comb(0,0)
    0 != 3
    range i = [0]
    i = 0
    t[0] = a[0] = 1
    comb(1,1)
        1 != 3
        range i = [1]
        i = 1
        t[1] = a[1] = 2
        comb(2,2)
            2 != 3
            range i = [2]
            i = 2
            t[2] = a[2] = 3
- - - - 
R  = 2
N = 3
a = [1,2,3]
t = [0]*2 
comb(0,0)
    0 != 3
    range i = [0, 1]
    i = 0
    t[0] = a[0]
    comb(1,1)
    ---
        1 != 3
        range i = [1,2]
        i = 1
        t[1] = a[1]
        comb(2,2)
            2 != 3
            range i = [2,3]
            i = 2
            t[2] = a[2]
            comb(3,3)
                3 == 3
                print(t)

            i = 3 
            t[2] = a[3]
            comb(3,4)
                print(t)
        i = 2
        t[1] a[2]
        comb(2,3)
            2 != 3
            range i = [2,3]
            i = 2
            t[2] = a[2]
            comb(3,3)
                print(t)

            i = 3
            t[2] = a[3]
            comb(2,4)


    i = 1
    t[0] = a[1]
    comb(1,2)








"""