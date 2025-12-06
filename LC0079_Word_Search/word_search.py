from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.visited = []

    def dfs(self, board: List[List[str]], word: str, x: int, y: int, idx: int):
        # base cases
        if idx == len(word):
            return True
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False
        if self.visited[x][y] or board[x][y] != word[idx]:
            return False
        
        self.visited[x][y] = True
        found = self.dfs(board, word, x, y - 1, idx + 1) or self.dfs(board, word, x - 1, y, idx + 1) or self.dfs(board, word, x, y + 1, idx + 1) or self.dfs(board, word, x + 1, y, idx + 1)
        self.visited[x][y] = False
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board) # number of rows
        self.n = len(board[0]) # number of columns
        for i in range(self.m):
            for j in range(self.n):
                # Try to search for word starting at (i, j)
                self.visited = [[False] * self.n for _ in range(self.m)]
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, 0):
                        return True
        return False
