# Programmers
# 스택/큐 기능개발
import math
progresses = [53, 30, 55]
speeds = [4, 4, 4]
def solution(progresses, speeds):
    answer = []
    def pass_day(progresses,speeds):
        completed_count = 0
        remain = 100 - progresses[0]
        passed_day =  math.ceil(remain/speeds[0])
        for idx,progress in enumerate(progresses):
            progresses[idx] += speeds[idx]*passed_day
        idx = 0
        while True:

            if progresses[idx] >= 100:
                completed_count += 1
                idx += 1
                if idx >= len(progresses):
                    break
            else:
                break
        return progresses[completed_count:], speeds[completed_count:],completed_count
    while len(progresses):
        progresses,speeds, cnt = pass_day(progresses,speeds)
        answer.append(cnt)
    return answer
print(solution(progresses, speeds))


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses):
        if progresses[0] + speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution(progresses, speeds))
