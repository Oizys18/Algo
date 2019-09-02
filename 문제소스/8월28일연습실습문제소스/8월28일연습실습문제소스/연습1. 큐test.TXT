# Q = [0] * 10
# f = r = -1
# def isEmpty() :
# 	return f == r
#
# def isFull() :
# 	return r == len(Q) - 1
#
# def enQ(item) :
# 	global r
# 	if isFull() : print('Queue_Full')
# 	else :
# 		r += 1
# 		Q[r] = item
#
# def deQ():
#     global f
#     if isEmpty() : print('Queue_Empty')
#     else :
#         f += 1
#         return Q[f]
#
# enQ(1)
# enQ(2)
# enQ(3)
# print(deQ())
# print(deQ())
# print(deQ())


Q = [0] * 10
f = r = -1
r += 1; Q[r] = 1
r += 1; Q[r] = 2
r += 1; Q[r] = 3

f += 1; print(Q[f])
f += 1; print(Q[f])
f += 1; print(Q[f])