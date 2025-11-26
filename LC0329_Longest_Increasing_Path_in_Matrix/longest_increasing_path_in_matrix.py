from collections import deque
from typing import List

class Vertex:
    def __init__(self, val):
        self.val = val
        self.outgoing = [] # list of vertices that this vertex has an edge pointing to
        self.incoming = [] # list of vertices that have an edge pointing to this vertex

class Edge:
    def __init__(self, src: Vertex, dest: Vertex, cost: int):
        self.src = src
        self.dest = dest
        self.cost = cost

# directed adjacency list representation of a graph   
class Graph:
    # Construct a directed graph given a matrix
    # Every vertex has a list of incoming edges and a list of outgoing edges
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix) # number of rows
        self.n = len(matrix[0]) # number of columns
        self.vertices = {} # maps coordinates to the vertex
        #self.edges = []

        # Create vertices for each cell in the matrix
        for i in range(self.m):
            for j in range(self.n):
                vertex = Vertex(matrix[i][j])
                self.vertices[(i, j)] = vertex
        
        # Create edges 
        for i in range(self.m):
            for j in range(self.n): 
                curr_vtx = self.vertices[(i, j)]
                # Check the right neighbor
                if j + 1 < self.n:
                    right_vtx = self.vertices[(i, j + 1)]
                    if curr_vtx.val < right_vtx.val:
                        self.add_edge(curr_vtx, right_vtx)
                # Check the bottom neighbor
                if i + 1 < self.m:
                    bottom_vtx = self.vertices[(i + 1, j)]
                    if curr_vtx.val < bottom_vtx.val:
                        self.add_edge(curr_vtx, bottom_vtx)
                # Check the left neighbor
                if j - 1 >= 0:
                    left_vtx = self.vertices[(i, j - 1)]
                    if curr_vtx.val < left_vtx.val:
                        self.add_edge(curr_vtx, left_vtx)
                # Check the top neighbor
                if i - 1 >= 0:
                    top_vtx = self.vertices[(i - 1, j)]
                    if curr_vtx.val < top_vtx.val:
                        self.add_edge(curr_vtx, top_vtx)

    # add a directed edge from src to dest
    def add_edge(self, src: Vertex, dest: Vertex):
        #edge = Edge(src, dest, -1)
        #self.edges.append(edge)
        src.outgoing.append(dest)
        dest.incoming.append(src)

    # checks if the graph is properly constructed
    def graph_info(self):
        for k, v in self.vertices.items():
            curr_vtx = self.vertices[k]
            print(f"\n------{k}: {curr_vtx.val}------")

            # Print all outgoing vertices of curr_vtx
            print("---Outgoing vertices---")
            for outgoing_vtx in curr_vtx.outgoing:
                print(f"{outgoing_vtx.val}")

            # Print all incoming vertices of curr_vtx
            print("\n---Incoming vertices---")
            for incoming_vtx in curr_vtx.incoming:
                print(f"{incoming_vtx.val}")

    def dfs(self, start_vtx: Vertex, memo: dict):
        if start_vtx in memo.keys():
            return memo[start_vtx]
        
        if len(start_vtx.outgoing) == 0:
            memo[start_vtx] = 1
            return 1
        
        max_dist = 0
        for nbr in start_vtx.outgoing:
            max_dist = max(max_dist, self.dfs(nbr, memo))
        memo[start_vtx] = max_dist + 1
        return memo[start_vtx]

        # queue = deque()
        # distances = {start_vtx: 0}
        # queue.append(start_vtx)
        # #furthest_vtx = start_vtx
        # max_dist = 0
        # while len(queue) > 0:
        #     curr_vtx = queue.popleft()
        #     # Examine all the outgoing vertices of curr_vtx
        #     for nbr in curr_vtx.outgoing:
        #         queue.append(nbr)
        #         distances[nbr] = distances[curr_vtx] + 1
        #         # Also keep track of the furthest vertex from start_vtx
        #         max_dist = max(max_dist, distances[nbr])
        # return max_dist + 1


    def longest_increasing_path(self):
        # Consider each vertex as a starting vertex for BFS.
        max_path_length = 0
        memo = {}
        for vtx in self.vertices.values():
            # u, _ = self.bfs(vtx)
            # _, max_dist = self.bfs(u)
            # Only consider vertices with no incoming edges
            if len(vtx.incoming) == 0:
                max_dist = self.dfs(vtx, memo)
                max_path_length = max(max_path_length, max_dist)
        return max_path_length

    # Run Bellman-Ford on the graph from start_vtx. At the same time, return the lowest cost (i.e. most negative) of any path from start_vtx.
    def bellman_ford(self, start_vtx: Vertex):
        V = len(self.vertices.values()) # V = number of vertices in the graph
        dist = {vtx: 1000 for vtx in self.vertices.values()} # maps vertex to the shortest distance from src_vtx to it
        dist[start_vtx] = 0
        updated = False # tracks if there was an update made to dist in a particular iteration
        lowest_cost = float('inf')
        for i in range(V):
            updated = False
            for edge in self.edges:
                if dist[edge.src] != 1000 and dist[edge.src] + edge.cost < dist[edge.dest]:
                    # If we're at the V-th iteration, then there is a negative cycle
                    if i == V - 1:
                        raise Exception("Negative cycle detected in the graph")
                    # Update shortest distance from edge.src to edge.dest
                    dist[edge.dest] = dist[edge.src] + edge.cost
                    lowest_cost = min(lowest_cost, dist[edge.dest])
                    updated = True
            # We can end the algorithm early if there are no updates made to dist in a particular iteration.
            if not updated:
                break
        return dist, min(lowest_cost, 0)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # trivial case
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return 1

        graph = Graph(matrix)
        return graph.longest_increasing_path()