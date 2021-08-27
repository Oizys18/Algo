def solution(progresses, speeds):
    answer = []
    day = 1 
    cnt = 0
    while progresses:
        if progresses[0] + speeds[0]*day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1 
        else:
            day += 1
            if cnt:
                answer.append(cnt)
                cnt = 0 
    answer.append(cnt)        
    return answer

"""
과거 JS로 풀었던 방식으로 Python으로 다시 풀이했다. 
progress와 speeds의 index 0을 확인하고 만약 조건에 부합하면 pop한다. 
아니라면 day를 증가시키고, cnt가 존재한다면(이전 day에서 조건에 부합하는 progress들이 있었다면)
answer에 append한다. 

마지막으로 line 15에서 마지막 progress를 추가시킨다. 
"""