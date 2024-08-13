class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx=0
        res=0

        for i in range(len(arr)):
            mx=max(mx,arr[i])
            if i==mx:
                res+=1
        return res
        