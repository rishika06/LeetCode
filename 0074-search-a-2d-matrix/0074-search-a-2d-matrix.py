class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        t = m * n #Considering our matrix to be flat, total_no_elements = (rows * cols) - 1 
        l, r = 0, t-1 #pointers for binary search

        while l <= r:
            m = (l + r) // 2
            i = m // n # row
            j = m % n # col

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif mid_num < target:
                l = m + 1
            else:
                r = m - 1
        
        return False