q = [0] * 100
f = r = -1
candis = 20
studcan = [1] * 20

sn = 1
nextsn = 2

r += 1; q[r] = sn

while candis > 0:
    f += 1;  sn = q[f]
    candis -= studcan[sn]
    studcan[sn] += 1

    if candis <= 0:
        print("%d번 학생이 마지막 사탕을 받아간다."%sn)
        break

    r += 1; q[r] = sn
    r += 1; q[r] = nextsn

    nextsn += 1


#
# q = [0] * 100
# f = r = -1
# candis = 20
# studcan = [1] * 20
#
# sn = 1
# nextsn = 2
#
# r += 1; q[r] = sn
# print("==>%d번 학생 : 입장하여 줄을 선다."%sn)
# print("학생 줄 : " , q[f+1:r+1])
#
# f += 1; sn = q[f]
# print("%d번 학생 : 줄에서 나와..."%sn)
# print("학생 줄 : " , q[f+1:r+1])
#
#
# while candis > 0:
#     if candis > studcan[sn] : candis -= studcan[sn]
#     else: studcan[sn] = candis; candis -= studcan[sn]
#     print("%d번 학생 : 선생님한테 사탕 %d개를 받는다."%(sn, studcan[sn]))
#     print("===== 남은 사탕의 개수는 %d개다."%candis)
#     print()
#     studcan[sn] += 1
#
#     if candis <= 0:
#         print("%d번 학생이 마지막 사탕을 받아간다."%sn)
#         break
#
#     r += 1; q[r] = sn
#
#     print("%d번 학생 : 다시 줄을 선다."%sn)
#     print("학생 줄 : ", q[f + 1:r + 1])
#     print("==> %d번 학생 : 입장하여 줄을 선다."%nextsn)
#
#     r += 1; q[r] = nextsn;
#     print("학생 줄 : ", q[f + 1:r + 1])
#
#     nextsn += 1
#     f += 1; sn = q[f]
#     print("%d번 학생 : 줄에서 나와..."%sn)
#     print("학생 줄 : ", q[f + 1:r + 1])