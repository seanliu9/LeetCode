from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) # number of rows
        n = len(grid[0]) # number of columns
        
        # Keep track of rotten and non-rotten oranges.
        total_oranges = 0
        num_rotten_oranges = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if not grid[i][j] == 0:
                    total_oranges += 1
                if grid[i][j] == 2:
                    num_rotten_oranges += 1
                    queue.append(((i, j), 0))

        # Perform BFS to simulate the oranges rotting.
        answer = 0
        while queue:
            (curr_i, curr_j), curr_time = queue.popleft()
            answer = max(answer, curr_time)
            # Explore left neighbor (if it contains a non-rotten orange)
            if curr_j - 1 >= 0 and grid[curr_i][curr_j - 1] == 1:
                num_rotten_oranges += 1
                grid[curr_i][curr_j - 1] = 2
                queue.append(((curr_i, curr_j - 1), curr_time + 1))
            # Explore top neighbor (if it contains a non-rotten orange)
            if curr_i - 1 >= 0 and grid[curr_i - 1][curr_j] == 1:
                num_rotten_oranges += 1
                grid[curr_i - 1][curr_j] = 2
                queue.append(((curr_i - 1, curr_j), curr_time + 1))
            # Explore right neighbor (if it contains a non-rotten orange)
            if curr_j + 1 < n and grid[curr_i][curr_j + 1] == 1:
                num_rotten_oranges += 1
                grid[curr_i][curr_j + 1] = 2
                queue.append(((curr_i, curr_j + 1), curr_time + 1))
            # Explore bottom neighbor (if it contains a non-rotten orange)
            if curr_i + 1 < m and grid[curr_i + 1][curr_j] == 1:
                num_rotten_oranges += 1
                grid[curr_i + 1][curr_j] = 2
                queue.append(((curr_i + 1, curr_j), curr_time + 1))

        if num_rotten_oranges == total_oranges:
            return answer
        else: # if not all oranges can rot
            return -1