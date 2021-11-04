class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        minus = 0
        flag = 0
        for w in s:
            if w == " ":
                if flag:
                    break
                continue
            elif w == "+" or w == "-":
                if flag:
                    break
                ans += w
                flag = 1
            elif w.isdigit():
                ans += w
                flag = 1
            else:
                break
        if ans == '' or ans == '+' or ans == '-':
            return 0
        ans = int(ans)

        if ans < 0 and ans < -2**31:
            ans = -2**31
        elif ans > 0 and ans > 2**31-1:
            ans = 2**31 - 1
        return ans


""" 
엣지케이스한테 호되게 당했다.
앞으론 꼼꼼히 챙길 것 
"""
