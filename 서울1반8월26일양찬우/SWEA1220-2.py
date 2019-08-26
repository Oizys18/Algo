#SWEA1220
import sys
sys.stdin = open('input.txt','r')

"""def move(c):
    while c > 0 and c < 9:
        if mat[c][j] == 1 and mat[c+1][j] == 0:
            c += 1
        elif mat[c][j] == 2 and mat[c-1][j] == 0:
            c -= 1
        else: 
            return c


for T in range(1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    """
    # 1 이면 오른쪽 
    # 2 라면 왼쪽 
"""
for _ in range(5):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i > 0 and i < N-1:
                c = move(i)
                mat[i][j], mat[c][j] = mat[c][j] , mat[i][j]
            else:
                if i == 0 and mat[i][j] == 1:
                    mat[i][j] == 0
                elif i == N-1 and mat[i][j] == 2:
                    mat[i][j] == 0

for i in mat:
    print(i)
"""
        
            


# 1 은 아래로 
# 2 는 위로 
"""
line = [1,0,2,0,0,1,1,2,1,0]

stack = []
stack2 = []
for i in line:
1. len(stack) == 0 일 때 2 가 나오면 무시 
2. 1이 나오면 그냥 넣기 

라인을 다 넣었을 때 
for j in stack:
3. len(stack2)가 0일 때 stack1 pop 해서 1이 나오면 무시 
4. pop 해서 2가 나오면 stack2에 넣기 

stack2에서 
"""


def seive(line):
    stack = []
    stack2 = []
    for i in range(len(line)):
        if line[i] == 2:
            if len(stack):
                stack.append(line[i])
        if line[i] == 1:
            stack.append(line[i])
    for _ in range(len(stack)):
        if len(stack):
            if stack[-1] == 1:
                if len(stack2) == 0:
                    stack.pop()
                else:
                    stack2.append(stack[-1])
                    stack.pop()
            elif stack[-1] == 2:
                stack2.append(stack[-1])
                stack.pop()
    stack = [0]
    while len(stack2):
        node = stack2.pop()
        if node != stack[-1]:
            stack.append(node)
    return stack.count(1)        

for T in range(1,11):
    N = int(input())
    mat = list(zip(*[list(map(int,input().split())) for _ in range(N)]))
    result = 0
    for r in mat:
        result += seive(r)
    print("#{0} {1}".format(T,result))




"""
# 갓상우
for t in range(10):
    N = int(input())
    arr = [[*map(int, input().split())]for _ in range(N)]
    ans = 0
    for x in range(N):
        s = 0
        for y in range(N):
            if arr[y][x] == 1:
                s = 1
            elif s and arr[y][x] > 1:
                ans += 1
                s = 0
    print(f'#{t+1} {ans}')
"""

"""
#갓현호

for t in range(10):
    input()
    r = 0
    s = [False for _ in range(100)]
    for _ in range(100):
        for i, x in enumerate(map(int, input().split())):
            if x:
                if s[i] and x == 2:
                    r += 1
                s[i] = x & 1
    print(f'#{t + 1}', r)
"""