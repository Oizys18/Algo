def solution(food_times, k):
    answer = 0
    N = len(food_times)
    if k <= N :
        print(k)
    turn,remain = divmod(k,N)
    print(turn,remain)
    
        

    return answer