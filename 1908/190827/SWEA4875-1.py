import sys
sys.stdin = open('input3.txt','r')

def bt(mat, start):
    stack = []
    visit = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if pathFinder(node):
                stack.extend(pathFinder(node))
    return visit

def pathFinder(node):
    zeros = []
    pass



for T in range(int(input())):
    stack = []
    N = int(input())
    mat = [input() for _ in range(N)]

    start = (0,mat[0].index('3'))
    res = [mat[i[0]][i[1]] for i in bt(mat,start)]
    result = 0
    for j in res:
        if j == '2':
            result = 1
    print("#{0} {1}".format(T+1,result))
    
