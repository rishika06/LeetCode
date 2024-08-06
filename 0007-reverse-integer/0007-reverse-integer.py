class Solution:
    def reverse(self, n: int) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        
        sign = -1 if n<0 else 1
        n = abs(n)
        
        rev_num = 0
        while n!=0:
            last_digit = n%10
            rev_num = (rev_num * 10 ) + last_digit
            n = n // 10
            
            if rev_num > INT_MAX:
                return 0
            
        return sign * rev_num
        