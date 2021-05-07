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

import itertools
dice_info = [*map(int, input().split())]

# 점수판
score_board = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
               30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26, 0]
visit = [0]*33
map_info = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 29, 30, 31, 24, 25, 26, 20, 32],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 28, 24, 25, 26, 20, 32],
            [0, 1, 2, 3, 4, 5, 21, 22, 23, 24, 25, 26, 20, 32]]
result = 0
pawn = [[0, 0], [0, 0], [0, 0], [0, 0]]
scores = [0]*4

def solve(diceIDX):
    global result
    if diceIDX == 10:
        if result < sum(scores):
            result = sum(scores)
        return

    dice = dice_info[diceIDX]
    for i in range(4):
        flag = 0
        cur_map = pawn[i][0]
        cur_pos = pawn[i][1]
        if cur_pos == 32:
            continue

        nxt_map = cur_map
        nxt_pos = cur_pos
        nxt = map_info[cur_map].index(cur_pos) + dice
        if cur_map == 0:
            if nxt >= len(map_info[cur_map]):
                nxt_pos = 32
            else:
                nxt_pos = map_info[cur_map][nxt]
                if nxt_pos == 5:
                    nxt_map = 3
                elif nxt_pos == 10:
                    nxt_map = 2
                elif nxt_pos == 15:
                    nxt_map = 1
        else:
            if nxt >= len(map_info[cur_map]):
                nxt_pos = 32
            else:
                nxt_pos = map_info[cur_map][nxt]

        if nxt_pos != 32:
            for p in range(len(pawn)):
                if nxt_pos == pawn[p][1]:
                    flag = 1
        if flag:
            continue

        pawn[i][0] = nxt_map
        pawn[i][1] = nxt_pos
        scores[i] += score_board[nxt_pos]
        visit[nxt_pos] = 1

        solve(diceIDX + 1)
        
        visit[nxt_pos] = 0
        pawn[i][0] = cur_map
        pawn[i][1] = cur_pos
        scores[i] -= score_board[nxt_pos]

solve(0)
print(result)



# for pawn_choice in itertools.product(range(4),repeat=10):
#     pawn = [[0,0],[0,0],[0,0],[0,0]]
#     temp_res = 0
#     flag = 0
#     visit = [0]*33
#     # 주사위 별 움직이는 말
#     for pc in range(10):
#         pawn_map = pawn[pawn_choice[pc]][0]
#         pawn_pos = pawn[pawn_choice[pc]][1]
#         if pawn_pos != 32:
#             dice = dice_info[pc]
#             if pawn_map == 0:
#                 nxt = map_one.index(pawn_pos) + dice
#                 if nxt >= len(map_one):
#                     pawn[pawn_choice[pc]][1] = 32
#                     next_pos = 32
#                     visit[pawn_pos] = 0
#                 else:
#                     next_pos = map_one[nxt]
#                     if next_pos == 5:
#                         pawn[pawn_choice[pc]][0] = 3
#                     elif next_pos == 10:
#                         pawn[pawn_choice[pc]][0] = 2
#                     elif next_pos == 15:
#                         pawn[pawn_choice[pc]][0] = 1
#                     if visit[next_pos]:
#                         flag = 1
#                         break
#                     else:
#                         pawn[pawn_choice[pc]][1] = next_pos
#                         visit[pawn_pos] = 0
#                         visit[next_pos] = 1
#                 temp_res += score_board[next_pos]
#             elif pawn_map == 1:
#                 nxt = map_two.index(pawn_pos) + dice
#                 if nxt >= len(map_two):
#                     pawn[pawn_choice[pc]][1] = 32
#                     next_pos = 32
#                     visit[pawn_pos] = 0
#                 else:
#                     next_pos = map_two[nxt]
#                     if visit[next_pos]:
#                         flag = 1
#                         break
#                     else:
#                         pawn[pawn_choice[pc]][1] = next_pos
#                         visit[pawn_pos] = 0
#                         visit[next_pos] = 1
#                 temp_res += score_board[next_pos]
#             elif pawn_map == 2:
#                 nxt = map_three.index(pawn_pos) + dice
#                 if nxt >= len(map_three):
#                     pawn[pawn_choice[pc]][1] = 32
#                     next_pos = 32
#                     visit[pawn_pos] = 0
#                 else:
#                     next_pos = map_three[nxt]
#                     if visit[next_pos]:
#                         flag = 1
#                         break
#                     else:
#                         pawn[pawn_choice[pc]][1] = next_pos
#                         visit[pawn_pos] = 0
#                         visit[next_pos] = 1
#                 temp_res += score_board[next_pos]
#             elif pawn_map == 3:
#                 nxt = map_four.index(pawn_pos) + dice
#                 if nxt >= len(map_four):
#                     pawn[pawn_choice[pc]][1] = 32
#                     next_pos = 32
#                     visit[pawn_pos] = 0
#                 else:
#                     next_pos = map_four[nxt]
#                     if visit[next_pos]:
#                         flag = 1
#                         break
#                     else:
#                         pawn[pawn_choice[pc]][1] = next_pos
#                         visit[pawn_pos] = 0
#                         visit[next_pos] = 1
#                 temp_res += score_board[next_pos]
#         else:
#             flag = 1
#             break
#     if flag:
#         continue
#     if temp_res > result:
#         result = temp_res
# print(result)


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
