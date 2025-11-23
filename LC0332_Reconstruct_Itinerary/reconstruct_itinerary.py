from collections import deque
from typing import List

class Graph:
    def __init__(self, tickets: List[List[str]]):
        self.adj = {} # maps vertex to a list of vertices that it has outgoing edges to
        # Build the graph 
        for ticket in tickets:
            src, dest = ticket[0], ticket[1] 
            # Add edge to adjacency list
            if src not in self.adj:
                self.adj[src] = [dest]
            else:
                self.adj[src].append(dest)

        # Sort each vertex's adjacency list by reverse alphabetical order.
        for vtx in self.adj:
            self.adj[vtx].sort(reverse=True)

    def eulerian(self, start_vtx, itinerary):
        stack = deque()
        stack.append(start_vtx)

        while stack:
            curr_vtx = stack[-1]
            if curr_vtx in self.adj and self.adj[curr_vtx]:
                nbr = self.adj[curr_vtx].pop()  
                stack.append(nbr)  
            else:
                itinerary.append(stack.pop())

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = Graph(tickets)
        result = []
        graph.eulerian("JFK", result)
        return result[::-1]