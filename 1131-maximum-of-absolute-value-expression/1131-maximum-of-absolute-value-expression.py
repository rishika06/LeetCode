class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        result = float('-inf')
    
        for p, q in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            max_val = float('-inf')
            min_val = float('inf')
        
            for i in range(len(arr1)):
                expr_val = arr1[i] * p + arr2[i] * q + i
                max_val = max(max_val, expr_val)
                min_val = min(min_val, expr_val)
        
            result = max(result, max_val - min_val)
    
        return result
        
#         if len(arr1) < 2 or len(arr2) < 2 and len(arr2) <= 40000 and len(arr1) <= 40000:
#             return 0
    
#         for val in arr1 + arr2:
#             if val < -10**6 or val > 10**6:
#                 return 0
    
#         maxVal = 0
#         for i in range(len(arr1)):
#             for j in range(i + 1, len(arr2)):
#                 currVal = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
#                 if currVal > maxVal:
#                     maxVal = currVal
#         return maxVal