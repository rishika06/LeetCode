class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            # Include condidates[i]
            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])
            cur.pop()

            # Skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            
            backtrack(i+1, cur, total)
        backtrack(0, [], 0)
        return res
        