from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Perform DFS whenever we see an X
        m = len(board) # number of rows
        n = len(board[0]) # number of columns
        count = 0
        i = 0
        j = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # Determine if board[i][j] is the start of a new ship
                    # The start of a new ship has no 'X' directly above it or to its left
                    if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                        continue 
                    count += 1

        return count