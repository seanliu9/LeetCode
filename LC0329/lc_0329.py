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
        self.edges = []

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
        edge = Edge(src, dest, -1)
        self.edges.append(edge)
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

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    graph = Graph(matrix)
    #graph.graph_info()

    # After constructing the graph, run Bellman-Ford starting from each vertex.
    #bellman_ford_results = []
    overall_lowest_cost = float('inf')
    for vtx in graph.vertices.values():
        result, curr_lowest_cost = graph.bellman_ford(vtx)
        overall_lowest_cost = min(overall_lowest_cost, curr_lowest_cost)
    
    # # Now find the distance with the lowest cost (i.e. most negative distance) across all of bellman_ford_results.
    # lowest_cost = float('inf')
    # for res in bellman_ford_results:
    #     for vtx, distance in res.items():
    #         lowest_cost = min(lowest_cost, distance)

    # We need to return number of vertices involved in the lowest cost distance (i.e. number of cells in the original problem)
    return -overall_lowest_cost + 1 

def test1():
    matrix = [[9, 7, 4], [6, 3, 8], [2, 1, 5]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test2():
    matrix = [[1]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test3():
    matrix = [[1, 2, 3, 4, 5]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test4():
    matrix = [[5, 4, 3, 2, 1]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test5():
    matrix = [[1], [2], [3], [4], [5]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test6():
    matrix = [[5], [4], [3], [2], [1]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test7():
    matrix = [[2, 1, 5, 12], [4, 7, 8, 10]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test8():
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test9():
    matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test10():
    matrix = [[1, 2, 3], [6, 5, 4], [7, 8, 9], [12, 11, 10], [13, 14, 15]]
    answer = longestIncreasingPath(matrix)
    print(answer)

def test11():
    matrix = [[1, 6, 7, 12, 13], [2, 5, 8, 11, 14], [3, 4, 9, 10, 15]]
    answer = longestIncreasingPath(matrix)
    print(answer)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
