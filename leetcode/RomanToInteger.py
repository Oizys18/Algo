""" 
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Given a roman numeral, convert it to an integer.
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        N = len(s)
        pre = s[0]
        for i in range(1, N):
            if (pre == 'I' and s[i] in 'VX') or (pre == 'X' and s[i] in 'LC') or (pre == 'C' and s[i] in 'DM'):
                total -= roman_dict[pre]
            else:
                total += roman_dict[pre]
            pre = s[i]
        total += roman_dict[pre]
        return total


""" 
속도가 굉장히 빠르게 잘 나왔다. 97퍼 보다 빠름 
근데 다른사람 코드보니까 그리스식 숫자표기는 결국 큰 수부터 쓸 수 있어서 앞글자가 뒷글자보다 작으면 그냥 빼주면되더라. 
그래서 아래와 같이 고칠 수 있음 
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        rd = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        words = [rd[i] for i in s]
        N = len(s)
        for i in range(1, N):
            if words[i-1] < words[i]:
                total -= words[i-1]
            else:
                total += words[i-1]
        return total + words[i-1]


"""
근데 이렇게 쓰면 속도가 떨어짐 
"""
