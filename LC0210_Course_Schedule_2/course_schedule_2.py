from collections import deque
from typing import List
class Solution:
    # ordering is a dictionary that maps a vertex to its [preorder, postorder]
    def topo_sort(self, start_vtx: int, adj: dict, ordering: dict, clock: int, topo_order: deque) -> int:
        if ordering[start_vtx][0] != 0:
            return -1

        # Set preorder of start_vtx
        ordering[start_vtx][0] = clock
        clock += 1

        # Perform DFS on all the outgoing vertices of start_vtx.
        for nbr in adj[start_vtx]:
            if ordering[nbr][1] == 0:
                clock = self.topo_sort(nbr, adj, ordering, clock, topo_order)
                if clock == -1:
                    return -1

        ordering[start_vtx][1] = clock
        clock += 1
        topo_order.append(start_vtx)
        return clock

    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct a graph from prerequisites. An edge from u to v means u is a prereq for v.
        adj = {course: [] for course in range(numCourses)} # maps course number to the courses that it's a prereq for
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1] # b is a prereq of a
            if a == b: # self-loop
                return False
            adj[b].append(a)
        
        # Perform a topological sort of the graph
        topo_order = deque()
        ordering = {course: [0, 0] for course in range(numCourses)}
        clock = 1
        for i in range(numCourses):
            if ordering[i][0] == 0: # if course i hasn't been visited yet
                clock = self.topo_sort(i, adj, ordering, clock, topo_order)
                if clock == -1: # if it's not possible to finish all the courses
                    return []

        answer = []
        while topo_order:
            answer.append(topo_order.pop())
        return answer