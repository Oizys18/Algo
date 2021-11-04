class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        N = len(s)
        if N <= 1 :
            return s 
        def getMax(left,right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1 
                right += 1 
            return right - left - 1 
            

        start = end = 0 
        for i in range(N):
            max_str_1  = getMax(i,i)
            max_str_2  = getMax(i,i+1)
            max_str = max(max_str_1,max_str_2)
            if max_str > end-start:
                start = i - (max_str-1)//2 
                end = i + max_str//2
                print(i, max_str_1,max_str_2, max_str,s[start:end+1])
        return s[start:end+1]
""" 
brute force로 풀이시, O(N^3)의 시간복잡도를 가진다. (공간복잡도 O(N))

모든 palindrome은 대칭형태이기 때문에, 
각 인덱스에서 좌우를 비교하고 조금씩 늘려주는 방법을 사용하면 된다. 
단, 짝수 갯수의 palindrome도 가능하기 때문에 짝수를 체크해줘야해서 line 15~16에서 i,i와 i,i+1을 체크해준다. 
"""