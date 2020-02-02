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
for i in range(34):
    gameMap[i] = 0

# print(gameMap)



print([i for i in range(34)])
# start - 10 - 25 - 40 - finish
pathOne = [0, 1, 2, 3, 4, 5, 21, 22, 23, 24(25), 25, 26, 20(40), 33]
# start - 10pass - 20 - 25 - 40 - finish
pathTwo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 28, 24, 25, 26, 20, 33]
# start - 10pass - 20pass - 30 - 25 - 40 - finish
pathThree = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 29, 30, 31, 24, 25, 26, 20, 33 ]
# start - 10pass - 20pass - 30pass - 40 - finish 
pathFour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10(20), 11, 12, 13, 14, 15(30), 16, 17, 18, 19, 20(40), 33]









# pattern_1 = {}
# for i in range(21):
#     pattern_1[i] = 2*i
# pattern_2 = {}

