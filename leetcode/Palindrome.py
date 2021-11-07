class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x가 10일경우는 palindrome이 아니며 0일 경우 palindrome이다.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            # 뒤집기
            reverted = 0
            while x > reverted:
                reverted = reverted * 10 + x % 10
                x = x//10
            return x == reverted or x == reverted//10


""" 
파이썬이라서 날로먹은 감이..
단, str을 사용하지 않고 int로 비교하는 방법이 있다. 
x : int라면 
res = x%10
x /= 10 

이렇게하면 맨 뒤의 한 수씩 빼낼 수 있게된다. 

먼저 문제에서 음수로 '-'가 붙으면 무조건 palindrome이 아니라고 판단하기 때문에 x<0:return False, 
그리고 양수일 경우만 체크하면 된다. 

즉, N길이의 값이 있다면, N//2만큼의 길이만큼 빼내고 순서대로 비교해보면 된다. 

빼낸 수를 10을 곱하고 이전 수를 더하면 reverse한 값이 된다. 

단, 이 방법을 사용할 경우 palindrome이 홀수 길이일 경우를 생각해줘야한다. 
-> 마지막에 palindrome체크 시, revertedNumber/10을 하면 정중앙 값 하나를 지울 수 있다. 

*모든 결과는 int로 다뤄야함. 그냥 나누기하면 소숫점 발생 
"""
