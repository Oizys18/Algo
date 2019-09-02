#SWEA 4864 문자열 비교 


for T in range(int(input())):
    word = input()
    line = input()
    if word in line:
        print("#{0} {1}".format(T+1,1))
    else:
        print("#{0} {1}".format(T+1,0))



