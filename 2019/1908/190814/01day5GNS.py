# # SWEA 1221 GNS 

# # number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# # # lst = ['' for i in range(10)]
# # # print(lst)

# # def numArr(word):
# #     lst = ['' for i in range(10)]
# #     if word == "ZRO":
# #         lst[0] += word
# #     elif word == "ONE":
# #         lst[1] += word
# #     elif word == "TWO":
# #         lst[2] += word
# #     elif word == "THR":
# #         lst[3] += word
# #     elif word == "FOR":
# #         lst[4] += word
# #     elif word == "FIV":
# #         lst[5] += word
# #     elif word == "SIX":
# #         lst[6] += word
# #     elif word == "SVN":
# #         lst[7] += word
# #     elif word == "EGT":
# #         lst[8] += word
# #     elif word == "NIN":
# #         lst[9] += word


# for T in range(int(input())):
#     N,caseN = input().split()
#     print(N)
#     case = map(,input().split())
#     print(case)
#     lst = ['' for i in range(10)]
    
#     for i in case:
#         if i == "ZRO":
#             lst[0] += i + ' '
#         elif i == "ONE":
#             lst[1] += i + ' '
#         elif i == "TWO":
#             lst[2] += i + ' '
#         elif i == "THR":
#             lst[3] += i + ' '
#         elif i == "FOR":
#             lst[4] += i + ' '
#         elif i == "FIV":
#             lst[5] += i + ' '
#         elif i == "SIX":
#             lst[6] += i + ' '
#         elif i == "SVN":
#             lst[7] += i + ' '
#         elif i == "EGT":
#             lst[8] += i + ' '
#         elif i == "NIN":
#             lst[9] += i + ' '
#     result = ''.join(lst)
#     print(result)    

# a = 1<<10
# print(bin(a))

# from bisect import bisect_left
# def numArr(word, breakpoint=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]):
#     i = bisect_left(breakpoint, word)
#     return i

# arr = ['SVN', 'FOR', 'ZRO', 'NIN', 'FOR', 'EGT', 'EGT', 'TWO', 'FOR', 'FIV']

# print([numArr(word) for word in arr])



word_dict = {"ZRO":0, "ONE":1, "TWO":10, "THR":11, "FOR":100, "FIV":101, "SIX":110, "SVN":111, "EGT":1000, "NIN":1001}

# a = input().split()[0]
print('{FIV}'.format(**word_dict))



