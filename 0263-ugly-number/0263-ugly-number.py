class Solution:
    def isUgly(self, n: int) -> bool:       
        for num in [2, 3, 5]:
            while n > 1 and n % num == 0:
                n = n // num 
        
        if n == 1:
            return True
            
        return False
