#SWEA4047
import sys
sys.stdin = open('input2.txt','r')



# for card in cardDict.keys():
#     cardDict[card].extend([1,2,3,4,5,6,7,8,9,10,11,12,13])
# print(cardDict)

def collect(line):
    for i in range(0,len(line)-1,3):
        if int(line[i+1]+line[i+2]) not in cardDict[line[i]]:
            cardDict[line[i]].append(int(line[i+1]+line[i+2]))
        else:
            return False
    cnt = []
    for c in cardDict.values():
        cnt.append(13 - len(c))
    return cnt

for T in range(int(input())):
    line = input()
    temp_d = []
    cardDict = {
    'S':[],
    'D':[],
    'H':[],
    'C':[],
    }
    cnt = collect(line)
    if cnt:
        print("#{0}".format(T+1),end=' ')
        for c in cnt:
            print("{0}".format(c),end=' ')
        print()
    else:
        print("#{0} ERROR".format(T+1))



