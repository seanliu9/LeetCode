from typing import List
from collections import deque 

class Vertex:
    def __init__(self, id: int):
        self.id = id

# Every edge is unweighted.
class Edge:
    def __init__(self, src_vtx: Vertex, dest_vtx: Vertex):
        self.src_vtx = src_vtx
        self.dest_vtx = dest_vtx

class Graph:
    def __init__(self, adjacencies: List[List[int]]):
        self.vertices = {} # maps vertex id to its corresponding Vertex object
        self.adj = {} # maps vertex to a list of its outgoing edges
        num_vertices = 0
        for edge in adjacencies:
            u, v = edge[0], edge[1]
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

            self.adj[u_vtx].append(Edge(u_vtx, v_vtx))
            

        self.dist = [0] * num_vertices # dist[i] = shortest distance from root (whose id is 0) to vertex with id i
        self.visited = [False] * num_vertices 
    
    # Compute shortest path from root (id 0) to every vertex. Assume that every vertex is reachable from the root.
    def shortest_path(self):
        q = deque() # queue
        q.append(self.vertices[0])
        self.visited[0] = True
        while len(q) > 0:
            curr_vtx = q.popleft()
            # Scan all the unvisited outgoing vertices of curr_vtx
            for edge in self.adj[curr_vtx]:
                dest_vtx = edge.dest_vtx
                if not self.visited[dest_vtx.id]:
                    q.append(dest_vtx)
                    self.visited[dest_vtx.id] = True
                    self.dist[dest_vtx.id] = self.dist[curr_vtx.id] + 1

def test1():
    print("========== starting test 1 ==========")
    input = [[0, 1], [1, 2], [2, 3], [0, 3], [3, 6], [0, 4], [4, 5], [4, 2], [5, 2]]
    graph = Graph(input)
    graph.shortest_path()
    for i in range(len(graph.dist)):
        print(f"Node {i}'s shortest path from root: {graph.dist[i]}")
    print("========== finished test 1 ==========\n")

def test2():
    print("========== starting test 2 ==========")
    input = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]
    graph = Graph(input)
    graph.shortest_path()
    for i in range(len(graph.dist)):
        print(f"Node {i}'s shortest path from root: {graph.dist[i]}")
    print("========== finished test 2 ==========\n")

def test3():
    print("========== starting test 3 ==========")
    input = [[0, 1]]
    graph = Graph(input)
    graph.shortest_path()
    for i in range(len(graph.dist)):
        print(f"Node {i}'s shortest path from root: {graph.dist[i]}")
    print("========== finished test 3 ==========\n")

def test4():
    print("========== starting test 4 ==========")
    input = [[0, 1], [1, 2], [2, 0]]
    graph = Graph(input)
    graph.shortest_path()
    for i in range(len(graph.dist)):
        print(f"Node {i}'s shortest path from root: {graph.dist[i]}")
    print("========== finished test 4 ==========\n")

def test5():
    print("========== starting test 5 ==========")
    input = [[0, 1], [0, 3], [3, 0], [1, 2], [1, 4], [4, 2], [4, 5], [5, 6], [6, 7], [2, 7], [3, 2]]
    graph = Graph(input)
    graph.shortest_path()
    for i in range(len(graph.dist)):
        print(f"Node {i}'s shortest path from root: {graph.dist[i]}")
    print("========== finished test 5 ==========\n")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()





