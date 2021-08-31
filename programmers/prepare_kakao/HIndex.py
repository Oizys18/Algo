def solution(citations):
    answer = 0
    citations = sorted(citations)
    for idx, paper in enumerate(citations):
        if paper >= len(citations[idx:]):
            return len(citations[idx:])


def solution(citations):
    answer = 0
    citations.sort()
    N = len(citations)
    for H in range(1,max(citations)):
        for idx,cit in enumerate(citations):
            if cit >= H and N-idx >= H:
                if citations[:idx] and max(citations[:idx]) <= H:
                    answer = H
                else:answer = H 
            else:continue
    return answer 

"""
다시 푼 것이 아랫쪽 
-> H-index에 대해 완전히 이해를 하지 않고 푼 것 같다. 
결국 idx 0부터 본다면 H는 계속 작아질 수 밖에 없기 때문에, 
유효한 값이 나오자마자 break 하는 것이 옳다. 

아래코드는 효율성을 아슬아슬 통과한다. (시간 오래 걸림..!)
"""