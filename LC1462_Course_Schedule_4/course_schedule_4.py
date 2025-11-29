class Solution:
    def topo_sort(self, start_vtx: int, adj: dict, ordering: dict, clock: int) -> int:
        if ordering[start_vtx][0] != 0:
            return clock

        # Set preorder of start_vtx
        ordering[start_vtx][0] = clock
        clock += 1

        # Perform DFS on all outgoing vertices of start_vtx.
        for nbr in adj[start_vtx]:
            clock = self.topo_sort(nbr, adj, ordering, clock)

        # Set postorder of start_vtx
        ordering[start_vtx][1] = clock
        clock += 1
        
        return clock

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

        ordering = {i: [0, 0] for i in range(numCourses)}
        clock = 1
        for i in range(numCourses):
            if ordering[i][0] == 0:  # if course i hasn't been visited yet
                clock = self.topo_sort(i, adj, ordering, clock)

        answer = []
        for u, v in queries:
            if ordering[u][0] < ordering[v][0] and ordering[u][1] > ordering[v][1]:
                # (u, v) is a forward edge
                answer.append(True)
            elif ordering[v][0] < ordering[u][0] and ordering[v][1] > ordering[u][1]:
                # (u, v) is a back edge
                answer.append(False)
            else:
                # (u, v) is a cross edge
                visited = set()
                answer.append(self.dfs(adj, u, v, visited))

        return answer