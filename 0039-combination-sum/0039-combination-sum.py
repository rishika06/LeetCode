class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        nums = candidates
        n = len(nums)

        def backtrack(i, curr_sum):
            # I base case current sum = target
            if curr_sum == target:
                res.append(sol[:])
                return
            
            # II base case, current sum > target or length of list = i
            if curr_sum > target or i == n:
                return

            # Recursive solution
            # Not using the number
            backtrack(i+1, curr_sum)
            
            # Using the number
            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            sol.pop()
        
        backtrack(0, 0)
        return res


