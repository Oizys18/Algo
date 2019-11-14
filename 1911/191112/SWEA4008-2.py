# SWEA 4008 계산기
import sys
sys.stdin = open('4008.txt','r')
def calculator(res, depth, oper):
    pre = res
    # if depth == 0:
    #     pre = line[depth]
    
    post = line[depth+1]
    # print(pre, oper, post)
    # print(oper)
    dic = { 
        "+":(lambda a, b : a + b), 
        "-":(lambda a, b : a - b), 
        "*":(lambda a, b : a * b), 
        "/":(lambda a, b : int(a / b)), 
    }
    return dic[oper](pre,post)

import itertools
from pprint import pprint as pp
for T in range(int(input())):
    N = int(input())
    operator = list(map(int,input().split()))
    line = list(map(int,input().split()))
    minRes = 100000000
    maxRes = -100000000 
    res = 0
    temp = [0]*(N-1)

    def perm2(depth, operator, res=0):
        global minRes
        global maxRes
        if depth == N-1:
            # print(res)
            # print()
            if res <= minRes:
                minRes = res
            if res >= maxRes:
                maxRes = res
            return
        else:
            for i in range(4):
                if not operator[i]: continue
                operator[i] -= 1
                if i == 0:
                    temp = res
                    res = calculator(res,depth,'+')
                    perm2(depth+1, operator, res)
                    res = temp
                elif i == 1:
                    temp = res
                    res = calculator(res,depth,'-')
                    perm2(depth+1, operator, res)
                    res = temp
                elif i == 2:
                    temp = res
                    res = calculator(res,depth,'*')
                    perm2(depth+1, operator, res)
                    res = temp
                elif i == 3:
                    temp = res
                    res = calculator(res,depth,'/')
                    perm2(depth+1, operator, res)
                    res = temp                
                operator[i] += 1
    perm2(0,operator,line[0])
    print(f'#{T+1} {maxRes-minRes}')




    # def perm(depth, operator, res=0):
    #     if depth == N-1:
    #         print(res)
    #         return
    #     for i in range(len(operator)):
    #         if not operator[i]: continue
    #         print(operator)
    #         operator[i] -= 1
    #         if i == 0:
    #             temp = res = calculator(res, depth,'+')
    #             perm(depth+1,operator, res)
    #             res -= temp
    #         elif i == 1:
    #             res += calculator(res, depth,'-')
    #             perm(depth+1,operator)
    #             res -= calculator(depth,'-')
    #         elif i == 2:
    #             res += calculator(depth,'*')
    #             perm(depth+1,operator)
    #             res -= calculator(depth,'*')
    #         elif i == 3:
    #             res += calculator(depth,'/')
    #             perm(depth+1,operator)
    #             res -= calculator(depth,'/')
    #         operator[i] += 1
    # perm(0,operator)
            
            
            

                

"""
    def a(lst): # a.lst = [1,2,3]

        for i in range(len(lst)):
            lst[i] += 1
            
            a.lst = [2,2,3]

            a(lst)
                --> a.a.lst = [2,2,3]
                --> a.a.lst = [3,2,3]
                --> a(lst)
                    ...
                    return
            
            lst[i] -=1
            a.lst = [1,2,3]

    --------------------------------

    oper = [2,1,0,0]

    def solve(depth, oper):
        depth 1, oper [2,1,0,0]

        for i in range(4):
            if not oper[i]: continue

            oper[i] -=1     # oper = [1,1,0,0] +

            calc(i, num1, num2)

            solve(depth+1, oper)

                depth 2, oper [1,1,0,0]

                for i in range(4):
                    if ... continue
                    
                    oper[i] -= 1    # i=0, depth2_oper = [0,1,0,0] + + 

                    calc

                    solve(depth+1, oper) #solve(3, [0,1,0,0])
                        
                        for i in range(4):
                            if ... continue

                            oper[i] -= 1 # depth3_oper = [0,0,0,0] + + -

                            calc

                            solve() > return

                            oper[i] += 1 # depth3_opet = [0,1,0,0]
                        
                        return
                     
                    oper[i] += 1   # i=0, depth2_oper = [1,1,0,0] +

                next for
                    i = 1
                    if ... continue

                    oper[i] -= 1    # i=1, oper = [1,0,0,0] + -

                



            oper[i] +=1



"""



