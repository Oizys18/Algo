def solution(citations):
    answer = 0
    citations = sorted(citations)
    for idx, paper in enumerate(citations):
        if paper >= len(citations[idx:]):
            answer = len(citations[idx:])
            break
    
    return answer