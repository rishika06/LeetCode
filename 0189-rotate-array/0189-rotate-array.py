class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # ROTATION OF THE WHOLE ARRAY
        left, right = 0, n -1
        while left < right :
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        
        # ROTATION OF THE FIRST k ELEMENTS
        left, right = 0, k - 1
        while left < right :
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        
        # ROTATION OF THE LAST ELEMENTS
        left, right = k, n -1
        while left < right :
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
            