import sys
sys.stdin = open('input.txt', 'r')

def solve(s, e):
    if s == e:  return s
    else:
        win1 = solve(s, (s + e) // 2)
        win2 = solve((s + e) // 2 + 1, e)

        if card[win1] == card[win2]:
            return win1
        else:
            if card[win1] == 1:
                if card[win2] == 2:     return win2     # 가위 vs 바위
                else :                  return win1     # 가위 vs 보
            elif card[win1] == 2 :
                if card[win2] == 1:     return win1     # 바위 vs 가위
                else :                  return win2     # 바위 vs 보
            elif card[win1] == 3 :
                if card[win2] == 1:     return win2     # 보 vs 가위
                else :                  return win1     # 보 vs 바위

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    print('#%d'%tc, solve(1, N))
