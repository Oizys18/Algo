class Solution:
    def reverse(self, x: int) -> int:
        ans = int(''.join(reversed(str(abs(x)))))
        if ans >= 2**31-1:
            return 0
        if x < 0:
            return -1 * ans
        else:
            return ans


""" 
int를 한자리씩 pop 하는 방법. 

rev = 0
pop = x%10 
x /= 10 
temp = rev *10 +pop
rev = temp 

하지만, 
temp 연산시 문제의 숫자 제한 범위를 넘을 가능성이 있다. 
따라서 아래 연산을 해줘야한다. 
if rev > INT_MAX/10 or (rev == INT_MAX / 10 and pop > 7): return 0;
if rev < INT_MIN/10 or (rev == INT_MIN / 10 and pop < -8): return 0; 


단, 그냥 파이썬 식대로 풀어도 시간초과가 발생하지 않는다. 
아래는 ㄹㅇ 똑쟁이 코드 
"""


class Solution:
    def reverse(self, x: int) -> int:
        # x<0 이면 True==1이 되어 sign==-1  x>0이면 false==0이 되어 sign = 1
        sign = [1, -1][x < 0]
        ans = sign * int(str(abs(x))[::-1])
        return ans if -(2**31)-1 < ans < 2**31 else 0
