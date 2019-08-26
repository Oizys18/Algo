# Backtracking Powerset 
# 1~10의 powerset 중 원소 합이 10인 부분집합 모두 출력 

"""
def backtrack(a, k, put):
    c = [0] * put
    if k == put:
        return process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, put, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, put)    

def construct_candidates(a, k, put, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    temp = [] 
    for i in range(len(a)):
        if a[i] == True:
            temp.append(i)
    if sum(temp) == 10:
        print(temp) 

a = [0] * 11
put = 10
backtrack(a, 0, put)
"""

"""


def backtrack(k,sum):
    global cnt
    cnt += 1
    if k == N:
        if sum == 10:
            for i in range(1,11):
                if a[i] == True:
                    print(i, end= ' ')
            print()
    else:
        k += 1
        if sum + k <= 10:
            a[k] = 1; backtrack(k,sum + k)
        a[k] = 0; backtrack(k,sum)

N = 10
a = [0] * (N + 1)

cnt = 0 
backtrack(0, 0)
print(cnt)"""
"""
# cnt == 노드 수, 
# 만약 backtrack()의 else에서 
# 'if sum + k <= 10:'이 조건문이 없다면 2047, 
# 모든 조건을 다 계산함

# 조건문 추가시 cnt == 250 

# --> 완전탐색에서 점점 더 좋은, 효율적이고 빠른 탐색 : 
# 탐색공간을 줄이는 조건문을 추가해나가야함
"""
