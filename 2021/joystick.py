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


"""
1레벨이라고 써있지만 너무너무 어려웠다 ㅠ 

일단 오른쪽 끝에서 오른쪽 한 번 더 간다고 첫번쨰로 돌아가지 않는다는 점 ! (문제에서 왼쪽만 이동한다고 되어있음)
그리고 두번째로 0에서 시작할 때 가장 가까운 다음 순서를 골라야한다는 점이 중요하다 
사실 조이스틱에서 위아래로 움직여서 고르는 건 그냥 쉬움 
move함수는 왼쪽오른쪽, 위 아래 둘 다 써먹을 수 있었다 

"""