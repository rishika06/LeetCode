class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # If there is only one element, return it as the only permutation
        if len(nums) == 1:
            return [nums[:]]
        
        # Recursive case
        result = []

        for i in range(len(nums)):
            # remove the element at index i
            curr_nums = nums[i]
            remaining_nums = nums[:i] + nums[i+1:]

            # Recursively generate permutations for the remaining elements
            permutations_remaining = self.permute(remaining_nums)

            # Insert the remove element back into each permutation for all positions
            for permutation in permutations_remaining:
                result.append([curr_nums] + permutation)
                
        return result
        

    