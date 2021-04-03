lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[31, 10, 45, 1, 6, 19]
def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1


    def win(match):
        if match == 6:
            return 1
        elif match == 5:
            return 2
        elif match == 4:
            return 3
        elif match == 3:
            return 4
        elif match == 2:
            return 5
        elif match == 1 or match == 0:
            return 6
    answer = [win(zero+cnt),win(cnt)]

    return answer
print(solution(lottos,win_nums)) 