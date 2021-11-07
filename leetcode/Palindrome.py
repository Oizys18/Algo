class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s == s[::-1] else False


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
"""
# 뒤집는 방법
revertedNumber = 0
while x > revertedNumber:
    revertedNumber = revertedNumber * 10 + x % 10
    x /= 10
