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


# 새로 푼 풀이 
def solution(name):
    answer = 0
    N = len(name)
    wD = {v:k for k,v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    
    def change(idx):
        word = name[idx]
        if word!='A':
            if wD[word] < 26-wD[word]:
                return wD[word]
            return 26-wD[word] 
        return 0
        
    def howFar(i,j):
        if j-i > i + N-j-1 :
            return N-j+i
        else:
            return j-i
    
    idx = 0
    visit = [0 if i!='A' else 1 for i in name]
    while sum(visit)!=N:
        answer += change(idx)
        visit[idx] = 1 
        far = N
        nxt = 0
        for i in range(N):
            if not visit[i]:
                tfar = howFar(min(idx,i),max(idx,i))
                if far > tfar:
                    far = tfar
                    nxt = i
        if far != N:            
            answer += far 
            idx = nxt         
    return answer
"""
N-1 위치에서 오른쪽 커서로 idx 0으로 올 수 없다...!
line73에서 min max를 사용한 덕분에 얻어 걸린 듯 
 
"""