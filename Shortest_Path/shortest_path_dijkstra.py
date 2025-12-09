from typing import List
from collections import deque 
import heapq, itertools

class Vertex:
    def __init__(self, id: int):
        self.id = id
        self.dist_label = float('inf')
        self.predecessor = None # the edge that leads to this vertex in the shortest path from root to this vertex
        self.permanent = False

class Edge:
    def __init__(self, src_vtx: Vertex, dest_vtx: Vertex, weight: int):
        self.src_vtx = src_vtx
        self.dest_vtx = dest_vtx
        self.weight = weight

class Graph:
    def __init__(self, adjacencies: List[List[int]]):
        self.vertices = {} # maps vertex id to its corresponding Vertex object
        self.adj = {} # maps vertex to a list of its outgoing edges
        num_vertices = 0
        for edge in adjacencies:
            u, v, weight = edge[0], edge[1], edge[2]
            # Create or get the vertices corresponding to vertex id's u and v.
            if u not in self.vertices.keys():
                u_vtx = Vertex(u)
                self.vertices[u] = u_vtx
                self.adj[u_vtx] = []
                num_vertices += 1
            else:
                u_vtx = self.vertices[u]

            if v not in self.vertices.keys():
                v_vtx = Vertex(v)
                self.vertices[v] = v_vtx
                self.adj[v_vtx] = []
                num_vertices += 1
            else:
                v_vtx = self.vertices[v]

            self.adj[u_vtx].append(Edge(u_vtx, v_vtx, weight))
            

        # self.dist = [0] * num_vertices # dist[i] = shortest distance from root (whose id is 0) to vertex with id i
        # self.visited = [False] * num_vertices 
    
    # Compute shortest path from root (id 0) to every vertex. Assume that every vertex is reachable from the root.
    def shortest_path(self):
        counter = itertools.count() # breaks ties if multiple vertices in pq have the same distance label
        pq = [(0, next(counter), self.vertices[0])]
        heapq.heapify(pq)
        self.vertices[0].dist_label = 0
        while pq:
            curr_vtx = heapq.heappop(pq)[2]
            if not curr_vtx.permanent:
                curr_vtx.permanent = True
                # Scan all the non-permanent outgoing vertices of curr_vtx
                for edge in self.adj[curr_vtx]:
                    dest_vtx = edge.dest_vtx
                    if not dest_vtx.permanent:
                        new_dist_label = curr_vtx.dist_label + edge.weight
                        if new_dist_label < dest_vtx.dist_label:
                            dest_vtx.dist_label = curr_vtx.dist_label + edge.weight
                            dest_vtx.predecessor = edge
                            heapq.heappush(pq, (dest_vtx.dist_label, next(counter), dest_vtx))
    
    # This method should only be called after running shortest_path()
    def display_shortest_path_info(self):
        for i, vtx in self.vertices.items():
            if i == 0: # root has no predecessor
                print(f"Node {i}'s shortest path from root: {vtx.dist_label}")
            else:
                print(f"Node {i}'s shortest path from root: {vtx.dist_label}, predecessor edge: {vtx.predecessor.src_vtx.id} -> {vtx.predecessor.dest_vtx.id}")

def test1():
    print("========== starting test 1 ==========")
    input = [[0, 1, 1000], [1, 0, 950]]
    graph = Graph(input)
    graph.shortest_path()
    graph.display_shortest_path_info()
    print("========== finished test 1 ==========\n")

def test2():
    print("========== starting test 2 ==========")
    input = [[0, 1, 10], [1, 2, 15], [1, 3, 15], [2, 3, 10], [3, 4, 60], [2, 4, 5]]
    graph = Graph(input)
    graph.shortest_path()
    graph.display_shortest_path_info()
    print("========== finished test 2 ==========\n")

def test3():
    print("========== starting test 3 ==========")
    input = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10]]
    graph = Graph(input)
    graph.shortest_path()
    graph.display_shortest_path_info()
    print("========== finished test 3 ==========\n")

def test4():
    print("========== starting test 4 ==========")
    input = [[0, 1, 30], [1, 2, 40], [2, 3, 50], [0, 3, 5], [1, 0, 10], [2, 1, 10], [3, 2, 10]]
    graph = Graph(input)
    graph.shortest_path()
    graph.display_shortest_path_info()
    print("========== finished test 4 ==========\n")

def test5():
    print("========== starting test 5 ==========")
    input = [[0, 1, 50], [1, 2, 50], [2, 3, 50], [0, 3, 200], [3, 6, 10], [0, 4, 10], [4, 5, 5], [4, 2, 20], [5, 2, 5]]
    graph = Graph(input)
    graph.shortest_path()
    graph.display_shortest_path_info()
    print("========== finished test 5 ==========\n")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()