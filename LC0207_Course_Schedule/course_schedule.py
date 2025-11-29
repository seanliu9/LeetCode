from collections import deque
from typing import List

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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construct a graph from prerequisites. An edge from u to v means u is a prereq for v.
        adj = {course: [] for course in range(numCourses)} # maps course number to the courses that it's a prereq for
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1] # b is a prereq of a
            if a == b: # self-loop
                return False
            adj[b].append(a)
        
        # Perform a topological sort of the graph
        self.ordering = {course: [0, 0] for course in range(numCourses)}
        for i in range(numCourses):
            if self.ordering[i][0] == 0: # if course i hasn't been visited yet
                self.topo_sort(i, adj)
        #topo_order = list(self.topo_order)[::-1]

        # For each prereq, determine what type of edge it is. If it's a back edge, then we cannot finish all the courses.
        for u, v in prerequisites: # The policy says that v is a prereq of u.
            u_pre = self.ordering[u][0]
            u_post = self.ordering[u][1]
            v_pre = self.ordering[v][0]
            v_post = self.ordering[v][1]
            if u_pre < v_pre and u_post > v_post:
                return False

        return True