class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
    
        while top<= bottom and left <= right:
            # FILL THE TOP ROW
            for i in range(left, right+1):
                matrix[top][i]=num
                num+=1
            top += 1

            # FILL THE RIGHT COLUMN
            for i in range(top, bottom+1):
                matrix[i][right]=num
                num+=1
            right-=1

            # FILL THE BOTTOM ROW
            for i in range(right,left-1, -1):
                matrix[bottom][i]=num
                num+=1
            bottom -= 1

            # FILL THE LEFT COLUMN
            for i in range(bottom, top-1, -1):
                matrix[i][left]=num
                num+=1
            left += 1
            
            
        return matrix
        