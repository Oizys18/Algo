
# class arr:
#    a = ['Seoul','Kyouggi','Incheon','D어쩌구','D저쩌구','P어쩌구']
# str01=' ' #답안에서 빈칸이 있어 보였는데, 수기 답안이라 앞칸 비워놔도 티가 별로 안나서 초조함  
# for i in arr.a: # arr 클래스의 a 배열 값을 하나씩 추출 
#    str01 = str01 + i[0] # 추출한 값의 0번째 값
# print(str01)


# li2 = [[45,50,60],[89]] # 첫번째 배열 3번째 값은 잘 기억안남 
# print(len(li2[0])) # li2 배열 첫번째 값([45,50,60])의 길이 
# print(len(li2[1])) # li2 배열 두번째 값([89])의 길이 
# print(li2[0][0]) # li2 배열 첫번째 값([45,50,60])의 0번째 인자
# print(li2[0][1]) # li2 배열 첫번째 값([45,50,60])의 1번째 인자 
# print(li2[1][0]) # li2 배열 두번째 값([89])의 0번째 인자 


# i= j = 0 
# for i in range(0,6): # i -> 0,1,2,3,4,5 
#     j += i # i값을 추가해줌 
#     print(i,end='')
#     if i == 5:
#         print('=',end='') # 파이썬은 자동개행이라 추가함. 개행 안한게 정답 맞음  
#         print(j) # 모든 i 더한 값 
#     else:
#         print('+',end='') # i 가 0,1,2,3,4 일때 각각 +를 붙여줌 
# ㅁ

a = '12345'
a= list(a)
a[3] = 2
print(a[3])
a.pop(3)
a.insert(3,2)
print(a)