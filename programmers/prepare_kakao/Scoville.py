from heapq import * 

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville)>1:     
        first = heappop(scoville)
        if first >= K:
            break
            
        second = heappop(scoville)
        mixed = first + second*2 
        heappush(scoville,mixed)
        answer += 1 
    if min(scoville) < K:
        return -1 
    return answer

"""
간단한 힙 문제 
"""