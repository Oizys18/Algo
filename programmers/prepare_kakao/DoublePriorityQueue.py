from heapq import *
def solution(operations):
    answer = []
    q = []
    heapify(q)
    for operation in operations:
        work,num = operation.split()
        if work =='I':
            heappush(q,int(num))
        elif q:
            if  num =='1':
                # 최댓값 삭제
                q.sort()
                q.pop()
            else:
                # 최솟값 삭제
                heappop(q)
    if q: return [max(q),min(q)]
    else:return [0,0]
