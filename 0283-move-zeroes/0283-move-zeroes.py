class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # INITIALIZE THE POINTER FOR THE POSITION OF THE FIRST ZERO
        zero_pos = 0

        # TRAVERSE THE ARRAY
        for i in range (len(nums)):
            if nums[i] !=0:
                # SWAP THE NON-ZERO ELEMENT WITH THE ELEMENT AT THE zero_pos
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                # MOVE THE zero_pos POINTER TO THE NEXT POSITION
                zero_pos +=1