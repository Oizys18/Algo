"""
04/23/2021 19:38	Accepted	48 ms	14.4 MB	python3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = ''
        for w in s:
            if w in temp:
                ans = max(ans,len(temp))
                temp = temp[temp.index(w)+1:] + w
            else:
                temp += w
        ans = max(ans,len(temp))
        return ans
