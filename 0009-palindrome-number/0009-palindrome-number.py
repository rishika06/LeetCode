class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0 :
            return False
        
        original_num = n
        rev_num = 0
        
        while n != 0:
            last_digit = n % 10
            rev_num = rev_num * 10 + last_digit
            n = n // 10
        
        return rev_num == original_num