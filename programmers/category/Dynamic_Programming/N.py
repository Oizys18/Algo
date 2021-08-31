N = 9
number = 12
# # 444 / 4  = 111




def solution(N, number):
    answer = 0
    NN = int(str(N)*2)
    NNN = int(str(N)*3)
    NNNN = int(str(N)*4)
    NNNNN = int(str(N)*5)
    calc = {
        '+1': lambda x: x+1,
        '+11': lambda x: x+11,
        '+111': lambda x: x+111,
        '+1111': lambda x: x+1111,
        '+': lambda x: x+N,
        '++': lambda x: x+NN,
        '+++': lambda x: x+NNN,
        '++++': lambda x: x+NNNN,
        '*': lambda x: x*N,
        '**': lambda x: x*NN,
        '***': lambda x: x*NNN,
        '****': lambda x: x*NNNN,
        '*11': lambda x: x*11,
        '*111': lambda x: x*111,
        '*1111': lambda x: x*1111,
        '-': lambda x: x-N,
        '--': lambda x: x-NN,
        '---': lambda x: x-NNN,
        '----': lambda x: x-NNNN,
        '-1': lambda x: x-1,
        '-11': lambda x: x-11,
        '-111': lambda x: x-111,
        '-1111': lambda x: x-1111,
        '/': lambda x: x//N,
        '//': lambda x: x//NN,
        '///': lambda x: x//NNN,
        '////': lambda x: x//NNNN,
        '/11': lambda x: x//11,
        '/111': lambda x: x//111,
        '/1111': lambda x: x//1111,
    }

    memo = [0]*9

    def DP(pre, cnt):
        if cnt > 8:
            return
        if pre == number:
            if abs(memo[cnt]-number) > abs(pre-number):
                memo[cnt] = pre
            return
        if pre < 1-number or 32000 + number < pre:
            return
        if sum(memo) > 0:
            if cnt > min([i for i,x in enumerate(memo) if x]):
                return 
        if pre < number:
            DP(calc['+'](pre), cnt+1)
            DP(calc['++'](pre), cnt+2)
            DP(calc['+++'](pre), cnt+3)
            DP(calc['++++'](pre), cnt+4)
            DP(calc['+1'](pre), cnt+2)
            DP(calc['+11'](pre), cnt+3)
            DP(calc['+111'](pre), cnt+4)
            DP(calc['+1111'](pre), cnt+5)
            DP(calc['*'](pre), cnt+1)
            DP(calc['**'](pre), cnt+2)
            DP(calc['***'](pre), cnt+3)
            DP(calc['****'](pre), cnt+4)
            DP(calc['*11'](pre), cnt+3)
            DP(calc['*111'](pre), cnt+4)
            DP(calc['*1111'](pre), cnt+5)
        else:
            DP(calc['-'](pre), cnt+1)
            DP(calc['--'](pre), cnt+2)
            DP(calc['---'](pre), cnt+3)
            DP(calc['----'](pre), cnt+4)
            DP(calc['-1'](pre), cnt+2)
            DP(calc['-11'](pre), cnt+3)
            DP(calc['-111'](pre), cnt+4)
            DP(calc['-1111'](pre), cnt+5)
            DP(calc['/'](pre), cnt+1)
            DP(calc['//'](pre), cnt+2)
            DP(calc['///'](pre), cnt+3)
            DP(calc['////'](pre), cnt+4)
            DP(calc['/11'](pre), cnt+3)
            DP(calc['/111'](pre), cnt+4)
            DP(calc['/1111'](pre), cnt+5)
    DP(N, 1)
    DP(NN,2)
    DP(NNN,3)
    DP(NNNN,4)
    DP(NNNNN,5)
    for i,x in enumerate(memo):
        if x:
            answer = i
            break
    
    if answer > 8 or answer == 0:
        answer = -1
    return answer


print(solution(N, number))
# print(min([i for i,x in enumerate([0,0,3,2,2,1,1,5]) if x]))