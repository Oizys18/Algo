begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

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


print(solution(begin, target, words))
