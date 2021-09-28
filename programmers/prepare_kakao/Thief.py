from collections import defaultdict
def solution(money):
    answer = 0
    N = len(money)
    dp = defaultdict(int)
    bitmask = bin(1 << N)
    
    # print
    print(dp)
    print(bitmask)
    
     
    
    for i,v in enumerate(money):
        print(i,v)
    # 비트마스크로 풀기 
    
    return answer