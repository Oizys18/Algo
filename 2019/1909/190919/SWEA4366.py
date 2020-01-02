#SWEA4366




import sys, itertools
sys.stdin = open('input.txt','r')

def cnt(two_li,thr_li):
    for i in range(1,len(twos)):
        if two_li[i] == '0':
            two = int(''.join(two_li[:i]) + '1' + ''.join(two_li[i+1:]),2)
        elif two_li[i] == '1':
            two = int(''.join(two_li[:i]) + '0' + ''.join(two_li[i+1:]),2)
        for j in range(len(thrs)):
            if j == 0:
                for k in range(1,3):
                    if posThr[k] == thr_li[j]:
                        continue
                    thr = int(''.join(thr_li[:j]) + posThr[k] + ''.join(thr_li[j+1:]),3)
                    if two == thr:
                        return two
            else:
                for k in range(3):
                    if posThr[k] == thr_li[j]:
                        continue
                    thr = int(''.join(thr_li[:j]) + posThr[k] + ''.join(thr_li[j+1:]),3)
                    if two == thr:
                        return two

for T in range(int(input())):
    twos = input()
    thrs = input()
    # possibleNums = min(int(twos,2),int(thrs,3))
    two_li = [i for i in twos]
    thr_li = [j for j in thrs]
    posThr = ['0','1','2']
    print("#{} {}".format(T+1,cnt(two_li,thr_li)))

            # else:
            #     if thr_li[j] == '1':
            #         thr = ''.join(thr_li[:j]) + '2' + ''.join(thr_li[j+1:])
            #     elif thr_li[j] == '2':     
            #         thr = ''.join(thr_li[:j]) + '1' + ''.join(thr_li[j+1:]) 
            #     elif thr_li[j] == '0':     
            #         thr = ''.join(thr_li[:j]) + '1' + ''.join(thr_li[j+1:]) 

# print("#{} {}".format(T+1,res))


