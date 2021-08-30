from heapq import *
def solution(jobs):
    answer = 0
    free = 0
    N = len(jobs)
    while jobs:
        workload = []
        heapify(workload)
        for idx, job in enumerate(jobs):
            if job[0] <= free:
                heappush(workload,(job[1],idx))
        if workload:
            i = heappop(workload)[1]
            work = jobs.pop(i)
            answer += free - work[0] + work[1]
            free += work[1]
        else:free += 1 
    return answer//N

"""
jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
return = 72 

jobs = [[0, 5], [1, 2], [5, 5]]
return 6 

처음 Line 11에서 우선순위를 비교할 항목으로 free-job[0] + job[1], 즉 업무 완료까지의 평균 시간이 최소가 되는 업무를 
다음 업무로 지정하는 방식으로 했는데 제출시 1~12만 계속 틀렸다. 

이후 테스트 케이스를 질문찾기로 검색해서 오답이 발생하는 테케를 찾아냈는데, 
결국 차이점은 Line11에서 다음 업무로 무조건 소요시간이 적은 일을 넣는 것이었다. 
생각해보니 당장 현재 시간보다 먼저 요청이 들어와서 대기중인 경우, 업무가 가장 먼저 끝나는 것을 실행하는게 다른 업무들이 
큐에 먼저 들어올 수 있게 하는 방법인 것 같다. 
"""