N = 3
number = 23

def solution(N, number):
    answer = 0
    memo = [[] for _ in range(9)]
    possible_answer = [0]*9
    possible_answer[0] = 0 
    n = str(N)
    calc = {
        0: '+'+n,
        1: '-'+n,
        2: '*'+n,
        3: '//'+n,
        4: n,
    }

    def check(line, pre, cnt):
        if cnt > 8:
            return
        val = eval(line)
        if val == number:
            possible_answer[cnt] = 1
            return
        else:
            if val < 1-number or 32000 + number < val:
                return
            if (line, cnt) not in memo[cnt]:
                memo[cnt].append((line, cnt))
            else:
                return
            if val < number:
                check(line+calc[0], 0, cnt+1)
                check(line+calc[2], 2, cnt+1)
                if pre in [0, 1, 2, 3] and line != '0':
                    check(line+calc[4], 0, cnt+1)
            else:
                check(line+calc[1], 1, cnt+1)
                check(line+calc[3], 3, cnt+1)
            if line != '0':
                check(str(val),0,cnt)


    check(n, 0, 1)
    if not sum(possible_answer):
        return -1
    else:
        return min([i for i,x in enumerate(possible_answer) if x])


print(solution(N, number))
