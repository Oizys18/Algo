import string 
def solution(name):
    answer = 0
    length = len(name)
    word = 'A'*length
    alpha = string.ascii_uppercase
    
    def move(pre,nxt,length):
        if abs(pre-nxt) <= pre + (length - nxt):
            return abs(pre-nxt)
        else:
            return pre + length - nxt
        
    def cnt(alp):
        return alpha.index(alp)
    
    
    diff = []
    for i in range(length):
        if word[i] != name[i]:
            diff.append(i)
    visit = [0]*len(diff)
    
    
    for d in range(len(diff)):
        answer += move(cnt(word[diff[d]]),cnt(name[diff[d]]),26)
        
    pre = 0
    while sum(visit)!=len(diff):
        minD = 21
        nxt = 0
        for k in range(len(diff)):
            if not visit[k]:
                if move(pre,diff[k],length) < minD:
                    minD = move(pre,diff[k],length)
                    nxt = k
        visit[nxt] = 1
        answer += move(pre,diff[nxt],length)
        pre = diff[nxt]
        
    return answer