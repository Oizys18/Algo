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
