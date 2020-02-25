# 주사위 윷놀이 
"""
# Rules 
1. nums은 1부터 5까지만 있다...!
2. 이동하려는 칸에 이미 말이 있으면 이동할 수 없다.. .! 
3. 시작칸과 도착칸에 말이 이미 있어도 이동 불가하다 .. 
"""
# import itertools
# for itert in itertools.combinations_with_replacement(range(4),10):
#     print(itert)
    
dice_info = [*map(int,input().split())]

# 현재 i번째 말의 위치
pawn = [0]*4

# 현재 i번째 말이 있는 지도 정보 
pawn_map = [1]*4

# 점수판 
score_board = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,30,35,22,24,28,27,26,0]

# 현재 맵 위의 말 위치 
map_visit = [0]*33

# 주사위 사용정보
visit = [0]*10

map_one = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,32]
map_two = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,29,30,31,24,25,26,20,32]
map_three = [0,1,2,3,4,5,6,7,8,9,10,27,28,24,25,26,20,32]
map_four = [0,1,2,3,4,5,21,22,23,24,25,26,20,32]
res = 0

def solve():
    




# def solve(turn,score):
#     global res
#     if turn >= 10:
#         if score > res:
#             # print('------------')
#             res = score
#         return
#     else:
        
#         for i in range(4):
#             if pawn[i] != 32:
#                 if not visit[turn]:
#                     flag = 0
#                     cur = pawn[i]
#                     cur_map = pawn_map[i]
#                     visit[turn] = 1
#                     dice_num = dice_info[turn]
                    
                    
                    
#                     if pawn_map[i] == 1:
#                         next_num = map_one.index(pawn[i]) + dice_num
#                         if next_num >= len(map_one):
#                             pawn[i] = 32
#                             nxt = 32
#                         else:
#                             nxt = map_one[next_num]
#                             if not map_visit[map_one[nxt]]:
#                                 pawn[i] = map_one[nxt]
#                                 map_visit[map_one[nxt]] = 1
#                                 map_visit[cur] = 0
#                                 if nxt == 5:
#                                     pawn_map[i] = 4
#                                 elif nxt == 10:
#                                     pawn_map[i] = 3
#                                 elif nxt == 15:
#                                     pawn_map[i] = 2
#                             else:
#                                 flag = 1
#                     elif pawn_map[i] == 2:
#                         next_num = map_two.index(pawn[i]) + dice_num
#                         if next_num >= len(map_two):
#                             pawn[i] = 32
#                             nxt = 32

#                         else:
#                             nxt = map_two[next_num]
#                             if not map_visit[nxt]:
#                                 map_visit[nxt] = 1
#                                 map_visit[cur] = 0
#                                 pawn[i] = nxt
#                             else:
#                                 flag = 1
#                     elif pawn_map[i] == 3:
#                         next_num = map_three.index(pawn[i]) + dice_num
#                         if next_num >= len(map_three):
#                             pawn[i] = 32
#                             nxt = 32
#                         else:
#                             nxt = map_three[next_num]
#                             if not map_visit[nxt]:
#                                 map_visit[nxt] = 1
#                                 map_visit[cur] = 0
#                                 pawn[i] = nxt
#                             else:
#                                 flag = 1
#                     elif pawn_map[i] == 4:
#                         next_num = map_four.index(pawn[i]) + dice_num
#                         nxt = map_four[next_num]
#                         if next_num >= len(map_four):
#                             pawn[i] = 32
#                             nxt = 32
#                         else:
#                             if not map_visit[nxt]:
#                                 map_visit[nxt] = 1
#                                 map_visit[cur] = 0
#                                 pawn[i] = nxt
#                             else:
#                                 flag = 1
#                     if not flag:
#                         print('---------')
#                         print(turn,pawn)
#                         solve(turn + 1, score + score_board[nxt])
                    
                    
#                     pawn_map[i] = cur_map
#                     pawn[i] = cur
#                     map_visit[nxt] = 0
#                     solve(turn+1, score)
#                     visit[turn] = 0
# solve(0,0)

# # print(res)