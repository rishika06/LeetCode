class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # define the hashset
        # iterate over the list
        # check if the element is in the set
            # if yes, return TRUE
                # add it to the hashset
            # else return FALSE
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        


        
        # We will take two for loops and check every iteration for the pair of elemets
        # The solution will get accepted, but it will give TLE when we submit

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False


        # TC => O(n^2)  - because both the inner and outer loop with will run for n times
        # SC => O(1)    - becasue we have not used any extra space other than the input array 