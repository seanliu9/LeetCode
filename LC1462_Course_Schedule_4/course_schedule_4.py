from collections import deque

class Solution:
    def __init__(self):
        self.clock = 1
        self.ordering = {} # maps node to its [preorder, postorder]
        self.topo_order = deque()

    def topo_sort(self, start_vtx: str, adj: dict):
        # if start_vtx has already been visited
        if self.ordering[start_vtx][0] != 0:
            return

        # Set preorder of start_vtx
        self.ordering[start_vtx][0] = self.clock
        self.clock += 1

        # Perform DFS on all the outgoing vertices of start_vtx.
        for nbr in adj[start_vtx]:
            if self.ordering[nbr][1] == 0: # if the vertex hasn't been fully processed yet
                self.topo_sort(nbr, adj)

        self.ordering[start_vtx][1] = self.clock
        self.clock += 1
        self.topo_order.append(start_vtx)

    def dfs(self, adj: dict, start_vtx: int, end_vtx: int, visited: set) -> bool:
        # Perform DFS from start_vtx to try to reach end_vtx
        if start_vtx == end_vtx:
            return True
        visited.add(start_vtx)
        for nbr in adj[start_vtx]:
            if nbr not in visited:
                if self.dfs(adj, nbr, end_vtx, visited):
                    return True
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # Construct a graph from prerequisites. An edge from u to v means u is a prereq for v.
        adj = {course: [] for course in range(numCourses)} # maps course number to the courses that it's a prereq for
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1] # a is a prereq of b
            adj[a].append(b)

        self.ordering = {i: [0, 0] for i in range(numCourses)}
        for i in range(numCourses):
            if self.ordering[i][0] == 0:  # if course i hasn't been visited yet
                self.topo_sort(i, adj)

        answer = []
        for u, v in queries:
            if self.ordering[u][0] < self.ordering[v][0] and self.ordering[u][1] > self.ordering[v][1]:
                # (u, v) is a forward edge
                answer.append(True)
            elif self.ordering[v][0] < self.ordering[u][0] and self.ordering[v][1] > self.ordering[u][1]:
                # (u, v) is a back edge
                answer.append(False)
            else:
                # (u, v) is a cross edge
                visited = set()
                answer.append(self.dfs(adj, u, v, visited))

        return answer
