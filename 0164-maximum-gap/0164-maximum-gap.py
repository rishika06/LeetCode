class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
    
        sortedArr = sorted(nums)
        maxDiff = 0

        for i in range(1, len(sortedArr)):
            maxDiff = max(maxDiff, sortedArr[i] - sortedArr[i-1])
        return maxDiff 