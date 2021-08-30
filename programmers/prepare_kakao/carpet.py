def solution(brown, yellow):
    answer = []
#     y = row * col
#     b = 2* row + 2* col + 4 
    poss =set()
    for i in range(1,yellow//2+1):
        if not yellow%i and i <= yellow//i:
            poss.add(i) 
    poss.add(1)
    for j in poss:
        row = j
        col = yellow//row
        if brown == 2*row + 2*col + 4:
            answer = [col+2,row+2]
    return answer