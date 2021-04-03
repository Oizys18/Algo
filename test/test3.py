#             1     2       3         4        5       6       7         8 
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
def solution(enroll, referral, seller, amount):
    answer = []
    N = len(enroll)
    boss = [0]*(N+1)
    tempEarn = [0]*(N+1)

    for x in range(N):
        if referral[x] == '-':
            boss[x+1] = 0
        else:
            boss[x+1] = enroll.index(referral[x])+1
    boss[0] = -1
    def payFee(num,money):
            stack = []
            stack.append([num,money])
            while stack:
                cur = stack.pop(0)
                if boss[cur[0]]:
                    stack.append([boss[cur[0]],money*0.1])
                    tempEarn[cur[0]] += money
                else:
                    tempEarn[cur[0]] += money
            
    for idx,earn in enumerate(amount):
        sellerNum = enroll.index(seller[idx])+1
        earning = earn*100
        if boss[sellerNum]:
            tempEarn[sellerNum] += earning*0.9
            payFee(boss[sellerNum],earning*0.1)
        else:
            tempEarn[sellerNum] += earning*0.9
    answer = tempEarn[1:]
    return answer

print(solution(enroll,referral,seller,amount))

"""
-- 코드를 입력하세요
SELECT * FROM PLACES WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT (HOST_ID) > 1);
"""