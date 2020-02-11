# 주사위 윷놀이 
"""
# Rules 
1. nums은 1부터 5까지만 있다...!
2. 이동하려는 칸에 이미 말이 있으면 이동할 수 없다.. .! 
3. 시작칸과 도착칸에 말이 이미 있어도 이동 불가하다 .. 
"""
"""
start - 10 - 25 - 40 - finish 
start - 10pass - 20 - 25 - 40 - finish
start - 10pass - 20pass - 30 - 25 - 40 - finish
start - 10pass - 20pass - 30pass - 40 - finish 

"""
total_score = 0
# map은 0 ~ 33 : 0이 시작 , 33이 도착  
pawn_position = [-1,-1,-1,-1]
pawn_path = [-1,-1,-1,-1]
# dice_num = [*map(int,input().split())]
gameMap = {}
for i in range(1,34):
    gameMap[i] = 0

path_one = []
path_two = []
path_three = []
path_four = []
