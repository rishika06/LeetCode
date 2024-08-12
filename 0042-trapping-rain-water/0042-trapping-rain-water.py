class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        for i in range(n):
            res+= max(0, min(left[i], right[i]) - height[i])
        return res



















        # n = len(height)
        # res = 0

        # for i in range(n):
        #     left = 0
        #     right = 0
        #     for j in range(i):
        #         left = max(left, height[j])
        #     for j in range(n-1, i-1, -1):
        #         right = max(right, height[j])
        #     res += max(0, min(left, right) - height[i])
        # return res