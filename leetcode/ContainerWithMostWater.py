class Solution:
    # time limit exceeded
    def maxArea(self, height) -> int:
        answer = 0
        N = len(height)
        for i in range(N):
            for j in range(i+1, N):
                water = abs(j-i)*min(height[j], height[i])
                answer = max(water, answer)
        return answer

        #         for idx,H in enumerate(height):
        # [1,8,6,2,5,4,8,3,7]
        # 0,1
        # 1,8
        # 2,6
        # 3,2
        # 4,5
        # 5,4
        # 6,8
        # 7,3
        # 8,7

        # 1,8 / 6,8 / 8,7 / 2,6 / 4,5 / 5,4 / 7,3 / 0,1
