# 문제 개편 후 틀림, 이전에 푼 것 
def solution(N, number):
    answer = 0
    ansSet = [0, {N}]
    for i in range(2, 9):
        this_set = {int(str(N)*i)}
        for j in range(1,i):
            for x in ansSet[j]:
                for y in ansSet[i-j]:
                    this_set.add(x+y)
                    this_set.add(x-y)
                    this_set.add(y-x)
                    this_set.add(x*y)
                    if y != 0:
                        this_set.add(x//y)
                    if x != 0:
                        this_set.add(y//x)
        if number in this_set:
            return i
        ansSet.append(this_set)
    return -1



def solution(N, number):
    answer = 0
    dp = [0,{N}]
    for i in range(2,9):
        temp = {int(str(N)*i)}
        for j in range(1,i):
            for k in dp[j]:
                temp.add(N*k)
                temp.add(N+k)
                if k:
                    temp.add(N//k)
                if k > N:
                    temp.add(N-k)
        if number in temp:
            print(dp)
            return i
        dp.append(temp)
    
    # for k in range(1,9):
    #     temp = set()
    #     for i in dp:
    #         temp.add(int(str(N)*k))
    #         temp.add(i+N)
    #         temp.add(i//N)
    #         if i*N <= 32000*N:temp.add(i*N)
    #         if i-N >= 0:temp.add(i-N)
    #     if number in temp:return k
    #     dp = dp.union(temp)
    return -1