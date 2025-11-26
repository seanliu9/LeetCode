from typing import List

class Solution:
    # Recursively rotate a matrix whose upper left corner is (x, y) and edge length is n
    def rRotate(self, matrix: List[List[int]], x: int, y: int, n: int) -> None:
        # base case
        if n <= 1:
            return
        else:
            # Perform a 4-way swap for each group of 4 elements on the outer layer
            for i in range(n - 1):
                matrix[x][y + i], matrix[x + i][y + n - 1], matrix[x + n - 1][y + n - 1 - i], matrix[x + n - 1 - i][y] = matrix[x + n - 1 - i][y], matrix[x][y + i], matrix[x + i][y + n - 1], matrix[x + n - 1][y + n - 1 - i]

            # recursive call to the next inside layer
            self.rRotate(matrix, x + 1, y + 1, n - 2)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.rRotate(matrix, 0, 0, n)