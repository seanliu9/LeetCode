from typing import List
from collections import deque

class Solution:
    # Run BFS from (start_x, start_y), and find the greatest path length from it.
    def bfs(self, matrix: List[List[int]], start_x: int, start_y: int, m: int, n: int):
        queue = deque()
        distances = [[0] * n for _ in range(m)]
        distances[start_x][start_y] = 0
        queue.append((start_x, start_y))
        max_dist = 0
        while len(queue) > 0:
            curr_x, curr_y = queue.popleft()
            new_dist = distances[curr_x][curr_y] + 1
            # Consider all 4 of curr_vtx's valid neighbors (left, up, right, down)
            # left neighbor
            if curr_y - 1 >= 0 and matrix[curr_x][curr_y - 1] > matrix[curr_x][curr_y]:
                queue.append((curr_x, curr_y - 1))
                distances[curr_x][curr_y - 1] = new_dist
                max_dist = max(max_dist, new_dist)
            # top neighbor
            if curr_x - 1 >= 0 and matrix[curr_x - 1][curr_y] > matrix[curr_x][curr_y]:
                queue.append((curr_x - 1, curr_y))
                distances[curr_x - 1][curr_y] = new_dist
                max_dist = max(max_dist, new_dist)
            # right neighbor
            if curr_y + 1 < n and matrix[curr_x][curr_y + 1] > matrix[curr_x][curr_y]:
                queue.append((curr_x, curr_y + 1))
                distances[curr_x][curr_y + 1] = new_dist
                max_dist = max(max_dist, new_dist)
            # bottom neighbor
            if curr_x + 1 < m and matrix[curr_x + 1][curr_y] > matrix[curr_x][curr_y]:
                queue.append((curr_x + 1, curr_y))
                distances[curr_x + 1][curr_y] = new_dist
                max_dist = max(max_dist, new_dist)

        return max_dist + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # trivial case
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return 1

        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        LIP_length = -1
        for i in range(m):
            for j in range(n):
                LIP_length = max(LIP_length, self.bfs(matrix, i, j, m, n))
        return LIP_length
