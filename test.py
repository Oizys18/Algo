a = [0, 1, 3, 0, 4, 12, 0]
N = len(a)

for i in range(N):
    for j in range(i+1, N):
        if a[i] == 0 and a[j]:
            a[i], a[j] = a[j], a[i]
