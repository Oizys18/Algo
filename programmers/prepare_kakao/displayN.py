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
    return -1

# 해결, 다른사람 코드 참고함 
# 맨처음 과거 풀이처럼 푼 이유가 있었음 .
"""
N을 n개 써서 만들 수 있는 모든 가짓수를 Nn이라고한다면, 
N1 = 1 
N2 = N1*N1 + N1-N1 + N1+N1 + N1//N1 
N3 = N2*N1 + N2-N1 + N2+N1 + N2//N1 ..... 이다. 

즉 N 5개로 만들 수 있는 모든 수는 
N5 = N1+N4  + N2+N3 이다! 
그래서 가능한 모든 가짓수를 전부 더해줘야 한다. 
"""

def solution(N, number):
    if N == number:
        return 1
    
    answer = 0
    dp = [{int(str(N)*i)} if i else 0 for i in range(0,9)]
    for i in range(2,9):   
        for j in range(1,i):  
            for x in dp[j]:    
                for y in dp[i-j]:      
                    dp[i].add(x*y)
                    dp[i].add(x+y)
                    if x-y>0:dp[i].add(x-y)
                    if x: dp[i].add(y//x)
        if number in dp[i]:
            return i
    return -1
