import itertools
N = 3


# 비트
temp = [0]*3
def powerset2(s):
    x = len(s)
    for i in range(1 << x):
        for j in range(x):
            if i & (1 << j):
                temp[j] = s[j]
            else:
                temp[j] = 0
        print('temp:',temp)
        # print([s[j] for j in range(x) if (i & (1 << j))])

powerset2([1,2,3])





# 아무것도 선택X, 모두 선택 포함 0~N
print('---------아무것도 선택X, 모두 선택 포함 0~N') 
for i in itertools.chain.from_iterable(itertools.combinations(range(0,N+1),r) for r in range(N+1)):
    print(i)

# 최소 1개 선택~ N-1개 선택
print('---------최소 1개 선택~ N-1개 선택')
for i in itertools.chain.from_iterable(itertools.combinations(range(0,N+1),r) for r in range(1,N)):
    print(i)


