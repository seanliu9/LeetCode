from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.island_count = 0
        self.visited = []


    def dfs(self, grid: List[List[str]], start_x: int, start_y: int):
        stack = deque()
        stack.append((start_x, start_y))
        while len(stack) > 0:
            curr_cell = stack.pop()
            curr_x, curr_y = curr_cell
            self.visited[curr_x][curr_y] = True

            # right neighbor of curr_cell
            if curr_y + 1 < self.n and not self.visited[curr_x][curr_y + 1] and grid[curr_x][curr_y + 1] == "1":
                stack.append((curr_x, curr_y + 1))

            # bottom neighbor of curr_cell
            if curr_x + 1 < self.m and not self.visited[curr_x + 1][curr_y] and grid[curr_x + 1][curr_y] == "1":
                stack.append((curr_x + 1, curr_y))

            # left neighbor of curr_cell
            if curr_y - 1 >= 0 and not self.visited[curr_x][curr_y - 1] and grid[curr_x][curr_y - 1] == "1":
                stack.append((curr_x, curr_y - 1))
            
            # top neighbor of curr_cell
            if curr_x - 1 >= 0 and not self.visited[curr_x - 1][curr_y] and grid[curr_x - 1][curr_y] == "1":
                stack.append((curr_x - 1, curr_y))

        # Once the stack is empty, we have fully identified an island
        self.island_count += 1

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid) # number of rows
        self.n = len(grid[0]) # number of columns
        self.visited = [[False] * self.n for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    
        return self.island_count