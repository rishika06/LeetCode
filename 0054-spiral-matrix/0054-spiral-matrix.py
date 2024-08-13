class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:    
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # TRAVERSE FROM LEFT TO RIGHT
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # TRAVERSE FROM TOP TO BOTTOM
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
               # TRAVERSE FROM RIGHT TO LEFT
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # TRAVERSE FROM BOTTOM TO TOP
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
    
        return result