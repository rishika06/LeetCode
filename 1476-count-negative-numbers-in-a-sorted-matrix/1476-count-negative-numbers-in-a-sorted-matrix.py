class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # GET THE DIMENSIONS OF THE GRID
        m, n = len(grid), len(grid[0])
        # SET THE STARTING POINT AT THE TOP RIGHT CORNER OF THE GRID
        row, col = 0, n-1
        # INITIALIZE COUNTER FOR NEGATIVE NUMBERS
        count = 0

        # TRAVERSE THE GRID WHILE THE INDICES ARE WITHIN THE GRID BOUNDARIES
        while row < m and col >= 0:
            # IF THE CURRENT NUMBER IS NEGATIVE
            if grid[row][col] < 0:
                # COUNT ALL THE NUMBERS BELOW IT (AS THEY WILL BE NEGATIVE DUE TO SORTING) AND MOVE LEFT
                count += m - row
                col -=1
            # IF THE NUMBER IS NON-NEGATIVE, MOVE DOWN 
            else:
                row +=1
        # RETURN THE COUNT OF NEGATIVE NUMBERS 
        return count
