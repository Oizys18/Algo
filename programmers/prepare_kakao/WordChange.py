min_cnt = 10000
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visit = [0]*len(words)

    def diff_one(this, that):
        cnt = 0 
        for x in range(len(this)):
            if this[x] != that[x]:
                cnt += 1
            if cnt >= 2:
                return False
        if cnt == 1:
            return True

    def DFS(pre, cnt):
        global min_cnt
        if cnt >= len(words) or cnt >= min_cnt:
            return
        if pre == target:
            if cnt < min_cnt:
                min_cnt = cnt
            return
        for idx, word in enumerate(words):
            if diff_one(pre, word):
                DFS(word, cnt+1)

    DFS(begin, 0)
    answer = min_cnt
    return answer

# DFS로 풀었음 
def solution(begin, target, words):
    answer = 0
    N = len(begin)
    M = len(words)
    if target not in words:
        return 0 
    
    def diffOne(now,word):
        cnt = 0 
        for i in range(N):
            if now[i] != word[i]:
                cnt += 1
                if cnt > 1:return False
        return True
    
    mn = [M] 
    def solve(now,k,visit):
        if k > len(words) or k >= mn[0]:
            return 
        if now == target:
            mn[0] = min(k,mn[0])
            return 
        for i in range(M):
            if diffOne(now,words[i]) and not visit[i]:
                visit[i] = 1 
                solve(words[i],k+1,visit)
                visit[i] = 0
    solve(begin,0,[0]*M)
    return mn[0]

"""
과거 풀이와 비교했을 때, dfs에서 visit 체크를 해서 효율성이 높아졌다. 
또한 global 변수를 사용안한다. (리스트로 관리)
"""

"""
다른 사람들의 코드를 보니 bfs로 많이 풀었더라. 
문제를 다시 생각해보니 거리를 재는 문제라서 bfs로 푸는게 좋을지도.. 
"""

# BFS로 풀어봤다. 
def solution(begin, target, words):
    answer = 0
    N = len(begin)
    M = len(words)
    def diff(w1,w2):
        cnt = 0 
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1 
                if cnt > 1: return False 
        return cnt == 1
    
    q = []
    visit = [0]*M
    q.append((begin,0))
    while q:
        now,depth = q.pop(0)
        if now == target:
            answer = depth
        for i in range(M):
            if diff(now,words[i]) and not visit[i]:
                q.append((words[i],depth+1))
                visit[i]= 1
                
    return answer