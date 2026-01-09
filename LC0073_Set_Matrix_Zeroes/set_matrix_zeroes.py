from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns

        # Create flags to denote if the topmost row and leftmost column should be set to 0.

        top_row_has_zero = False
        for num in matrix[0]:
            if num == 0:
                top_row_has_zero = True
                break

        leftmost_column_has_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                leftmost_column_has_zero = True
                break
        
        # Iterate through matrix (excluding top row and leftmost column).
        # If we see a 0 at (i, j), then set (i, 0) and (0, j) to 0.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Using the top row and leftmost column as markers, set values outside of them to 0 (if necessary).
        # e.g. If matrix[3][0] = 0, then everything in row 3 must be set to 0

        # Check leftmost column
        for i in range(1, m):
            if matrix[i][0] == 0:
                # Set everything in the i-th row to 0.
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Check top row
        for j in range(1, n):
            if matrix[0][j] == 0:
                # Set everything in the j-th column to 0.
                for i in range(1, m):
                    matrix[i][j] = 0

        # Check the 2 flags
        if top_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if leftmost_column_has_zero:
            for i in range(m):
                matrix[i][0] = 0