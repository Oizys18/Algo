#SWEA 4835.구간합

for case in range(int(input())):
    N,M = map(int,input().split())
    num_list = list(map(int,input().split()))

    sum_list = []
    for i in range(N-M+1):
        sum_list += [sum(num_list[i:i+M])]

    for j in range(len(sum_list)-1,0,-1):
        for k in range(0,j):
            if sum_list[k] > sum_list[k+1]:
                sum_list[k],sum_list[k+1] = sum_list[k+1],sum_list[k]

    result = sum_list[-1] - sum_list[0]
    print("#{0} {1}".format(case+1,result))