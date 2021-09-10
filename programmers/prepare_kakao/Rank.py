from collections import defaultdict
def solution(n, results):
    answer = 0
    results.sort()
    win = defaultdict(set)
    lose = defaultdict(set)
    for w,l in results:
        win[w].add(l)
        lose[l].add(w)

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (k in win[i] and j in win[k]): 
                    win[i].add(j)
                if (k in lose[i] and j in lose[k]):
                    lose[i].add(j)
                    
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1 
    return answer


"""
플루이드-와샬의 변형 (?)

-> 중간의 다리역할을 하는 k가 중요하다. 
i - j 의 관계는 i-k 와 k-j 의 상황에 맞춰 계속 업데이트 되어야한다. 

"""

"""
다른 사람 풀이, set의 update를 사용했다. 
결국은 k를 사용한 것과 비슷하지만, 
i에게 이긴 winner마다 i가 이긴 사람들의 정보를 추가해준다. 
(i가 j를 이겼다면, j가 이긴 사람들은 i도 이길 수 있다.)

마찬가지로 i에게 진 loser마다 i가 진 사람들의 정보를 추가해준다. 

곰곰히 생각하면 이해하겠는데 막상 이렇게 코드를 짜는 건 고민해야가능할듯.. ㅠ
"""
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer