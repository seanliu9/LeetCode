from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.visited = []
        self.adj = {} # maps coordinate to list of tuples (representing its adjacent coordinates)
        self.can_reach_pacific = set() 
        self.can_reach_atlantic = set()
        #self.reachable = {} # maps coordinate to tuple (1st element = can reach P, 2nd element = can reach)

    # Perform dfs from cell (x, y).
    def dfs(self, x, y, results):
        if self.visited[x][y]:
            return
        results.add((x, y))
        self.visited[x][y] = True
        # Explore each neighboring cell of (x, y) and add it to results.
        for neighbor in self.adj[(x, y)]:
            self.dfs(neighbor[0], neighbor[1], results)
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights) # number of rows
        self.n = len(heights[0]) # number of columns
        # trivial case
        if self.m == 1 and self.n == 1:
            return [[0, 0]]

        self.visited = [[False] * self.n for _ in range(self.m)]

        # Construct graph. There is an edge from u to v if u's height <= v's height.
        for i in range(self.m):
            for j in range(self.n):
                self.adj[(i, j)] = []
                # left neighbor
                if j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]:
                    self.adj[(i, j)].append((i, j - 1))
                # top neighbor
                if i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]:
                    self.adj[(i, j)].append((i - 1, j))
                # right neighbor
                if j + 1 < self.n and heights[i][j] <= heights[i][j + 1]:
                    self.adj[(i, j)].append((i, j + 1))
                # bottom neighbor
                if i + 1 < self.m and heights[i][j] <= heights[i + 1][j]:
                    self.adj[(i, j)].append((i + 1, j))
        # print("adjacency list:")
        # for k, v in self.adj.items():
        #     print(f"k: {k}, v: {v}")
        
        # Perform DFS from the Pacific-adjacent cells inward.
        # leftmost column
        for i in range(self.m):
            self.dfs(i, 0, self.can_reach_pacific)
        # top row
        for j in range(self.n):
            self.dfs(0, j, self.can_reach_pacific)
        #print("pacific: ", self.can_reach_pacific)

        # Perform DFS from the Atlantic-adjacent cells inward.
        self.visited = [[False] * self.n for _ in range(self.m)]
        # rightmost column
        for i in range(self.m):
            self.dfs(i, self.n - 1, self.can_reach_atlantic)
        # bottom row
        for j in range(self.n):
            self.dfs(self.m - 1, j, self.can_reach_atlantic)
        #print("atlantic:", self.can_reach_atlantic)

        # Take the intersection of the two sets
        return list(self.can_reach_pacific.intersection(self.can_reach_atlantic))

        