#더 맵게 힙 
scoville =[1, 2, 3, 9, 10, 12] 
K = 7
def solution(scoville, K):
    answer = 0
    hotdict = dict()
#     for idx, hot in enumerate(scoville):
#         if 
    return answer


# 1 -> v 
# 2   2 -> rr / vv 

# 3  3 -> vvv / 1 
#        vrr / rrv  2
 
# 5  4 -> vvvv / 1
#        vvrr / rrvv / vrrv 3
       # rrrr / 1  
# 8   5 -> vvvvv / 1
#        vvvrr / vvrrv / vrrvv / rrvvv / 4
#        vrrrr / rrvrr / rrrrv /  3 
# 13  6 -> vvvvvv / 1 
#       rrvvvv / vrrvvv / vvrrvv / vvvrrv / vvvvrr/   5 
#       rrrrvv /vrrrrv/ vvrrrr / rrvrrv / rrvvrr / vrrvrr/   6 
#       rrrrrr / 1
#  21   7 -> vvvvvvv / 1
#         vvvvvrr / vvvvrrv/ vvvrrvv/ vvrrvvv/ vrrvvvv/ rrvvvvv/  6
#         vvvrrrr/ vvrrvrr / vrrvvrr/ rrvvvrr / rrvvrrv / rrvrrvv / vrrvrrv / vvrrrrv / vrrrrvv/ rrrrvvv/  10
#         vrrrrrr / rrvrrrr/rrrrvrr/ rrrrrrv / 4
#         

#  n -> n-1 + n-2 