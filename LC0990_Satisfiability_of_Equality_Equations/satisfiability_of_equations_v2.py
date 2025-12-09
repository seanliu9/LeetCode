# This version finds strongly connected components (instead of union find).
from typing import List

class Vertex:
    def __init__(self, id: str):
        self.id = id
        self.visited = False
        self.comp_id = -1 # id of the connected component it belongs to

# undirected, unweighted graph
class Graph:
    def __init__(self, equations: List[str]):
        self.vertices = {} # maps variable name to its corresponding Vertex object
        self.adj = {} # maps Vertex object to its list of adjacent Vertices
        for equation in equations:
            #if equation[1] == "=":
            u, v = equation[0], equation[3]
            if u not in self.vertices.keys():
                u_vtx = Vertex(u)
                self.vertices[u] = u_vtx
                self.adj[u_vtx] = []
            if v not in self.vertices.keys():
                v_vtx = Vertex(v)
                self.vertices[v] = v_vtx
                self.adj[v_vtx] = []
            # Only add an edge between u and v if the input says u = v
            if equation[1] == "=":
                self.adj[self.vertices[u]].append(self.vertices[v])
                self.adj[self.vertices[v]].append(self.vertices[u])
        self.curr_comp_id = 0
    
    def dfs(self, start_vtx: Vertex):
        if not start_vtx.visited:
            start_vtx.visited = True
            start_vtx.comp_id = self.curr_comp_id
            for nbr in self.adj[start_vtx]:
                if not nbr.visited:
                    self.dfs(nbr)

    # After running this function, every vertex will have its comp_id match the ID of the connected component it belongs to.
    def find_connected_components(self):
        for _, curr_vtx in self.vertices.items():
            if not curr_vtx.visited:
                # Perform DFS and visit all the vertices reachable from curr_vtx
                self.dfs(curr_vtx)
                self.curr_comp_id += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Construct the graph from equations
        graph = Graph(equations)
        graph.find_connected_components()

        # For each inequality, check if the two variables belong to the same component. If so, immediately return False.
        for equation in equations:
            if equation[1] == "!":
                u, v = equation[0], equation[3]
                if graph.vertices[u].comp_id == graph.vertices[v].comp_id:
                    return False
        
        return True