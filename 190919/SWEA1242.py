#SWEA1242

import sys
sys.stdin = open('input2.txt','r')

def decom(n):
    if n == '0001101':
        return 0
    elif n == '0011001':
        return 1
    elif n == '0010011':
        return 2
    elif n == '0111101':
        return 3
    elif n == '0100011':
        return 4
    elif n == '0110001':
        return 5
    elif n == '0101111':
        return 6
    elif n == '0111011':
        return 7
    elif n == '0110111':
        return 8
    elif n == '0001011':
        return 9

def decode(password):
    passlen = len(password)
    while passlen != 56:
        passlen = len(password)
        if passlen < 56:
            password = '0'*(56-passlen) + password
        elif passlen > 56:
            while passlen % 56 != 0:
                passlen += 1
                if passlen % 56 == 0:
                    break
            n = passlen // 56
            passlen = len(password)
            ten = ''
            for t in range(0,passlen,n):
                ten += password[t] 
            password = ten
            # print(password)
        passlen = len(password)
    return password


for T in range(int(input())):
    N, M = map(int,input().split())
    codes = []
    for _ in range(N):
        codeline = input().lstrip('0').rstrip('0')
        if codeline not in codes and codeline:
            codes.append(codeline)
    # realCode = []
    # if T == 12:
    #     print(codes)            
    #     for l in codes:
    #         if '00000' in l:
    #             print(l)

    binCode = []
    for code in codes:
        binCode.append(bin(int(code,16))[2:])
    # realCode = []
    # for co in binCode:
    #     if '0000' in co:
    #         a = co.split('0000')
    #         for line in a:
    #             if line:
    #                 realCode.append(line)
    # print(real)
    result = 0
    for c in binCode:
        
        # if '0000000000' in c:
        #     print(c)
        #     c.rstrip('0')
        #     a = c.split('000000000')
        #     print(a)
        # if T==12:
        #     print(c)


        ten = c.rstrip('0')
        ten = decode(ten)
        odd = []
        even = []
        for j in range(8):
            if j == 7:
                vrf = decom(ten[0+7*j:7+7*j])
            elif j % 2 == 0:
                odd.append(decom(ten[0+7*j:7+7*j]))
            elif j % 2 != 0:
                even.append(decom(ten[0+7*j:7+7*j]))

        res = (sum(odd)*3) + sum(even) + vrf
        
        if res % 10 == 0:
            result += sum(odd) + sum(even) + vrf

    print("#{} {}".format(T+1, result))
    

# pw = []
# for _ in range(N):
#     line = input().strip('0')
#     if pw:
#         continue
#     else:
#         if line:
#             lineL = len(line)
#             if lineL < 56 : 
#                 pw = (56 - lineL)*'0' + line