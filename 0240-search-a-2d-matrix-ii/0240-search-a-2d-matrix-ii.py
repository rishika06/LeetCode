class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # DECLARE ROW AND COLUMNS
        # LOOP THROUGH THE MATRIX USING WHILE LOOP
        # IF TARGET IS MET RETURN TRUE
        # ELSE RETURN FALSE

        row=len(matrix)
        r=0
        c=len(matrix[0])-1

        while r<row and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r+=1
            else:
                c-=1
        return False

        # n = len(matrix)
        # for i in range(n):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False