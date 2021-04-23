# 프로그래머스, 권투시합, 크루스칼인듯 
def solution(n, results):
    answer = 0
    win = dict()
    lose = dict()
    for i in range(1,n+1):
        win[i] = set()
        lose[i] = set()
        
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
        
    for _ in range(2):
        for i in range(1,n+1):
            win_temp = set()
            for won in win[i]:
                win_temp = win_temp.union(win[won])
            win[i] = win[i].union(win_temp)

            lose_temp = set()
            for lost in lose[i]:
                lose_temp = lose_temp.union(lose[lost])
            lose[i] = lose[i].union(lose_temp)
        
    for l in range(1,n+1):
        if len(win[l]) + len(lose[l]) == n-1:
            answer += 1 
    
    return answer