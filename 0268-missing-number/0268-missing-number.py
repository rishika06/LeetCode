class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # APPROACH I
        # n = len(nums)

        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        
        # APPROACH II
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum