class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right:
            mid = left + ((right - left) // 2)

            # If mid element is greater than the rightmost element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # Otherwise, the minimum is in the left half (including mid)
            else:
                right = mid
        
        # When left == right, we have found the minimum element
        return nums[left]        


        