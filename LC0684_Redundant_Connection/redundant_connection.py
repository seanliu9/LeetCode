import heapq
from typing import List

class Solution:
    def findRedundantConnection_Prim(self, edges: List[List[int]]) -> List[int]:
        # Create undirected adjacency list representation of the graph
        # Get the vertices from the edges, and assign edge weights progressively.
        adj = {} # maps source id to a dictionary that maps destination id to connecting edge's weight
        #edge_weights = {}
        edge_wt = 1
        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in adj:
                adj[u] = {}
            if v not in adj:
                adj[v] = {}
            adj[u][v] = edge_wt
            adj[v][u] = edge_wt
            #edge_weights[tuple(edge)] = edge_wt
            edge_wt += 1
        V = len(adj.keys()) # V = number of vertices
        visited = [False] * (V + 1)
        pq = []
        total_wt = 0
        heapq.heappush(pq, (0, 1))
        while pq:
            wt, u = heapq.heappop(pq)
            if not visited[u]:
                visited[u] = True
                total_wt += wt
                # Scan the unvisited neighboring vertices of u
                for v in adj[u].keys():
                    if not visited[v]:
                        heapq.heappush(pq, (adj[u][v], v))
        idx = int((V * (V + 1)) / 2 - total_wt)
        return edges[idx - 1]
    
    def findRedundantConnection_Kruskal(self, edges: List[List[int]]) -> List[int]:
        # Start with a forest of n trees, each of which contains a single vertex
        trees = {} # maps vertex ID to the ID of the tree that it currently belongs to
        for edge in edges:
            u, v = edge[0], edge[1]
            if not u in trees.keys():
                trees[u] = u
            if not v in trees.keys():
                trees[v] = v
        # Scan all the edges. Adding an edge either connects 2 separate trees or creates a cycle.
        for edge in edges:
            u, v = edge[0], edge[1]
            u_tree_ID = trees[u]
            v_tree_ID = trees[v]
            if u_tree_ID == v_tree_ID: 
                # Adding an edge between 2 vertices in the same tree would create a cycle.
                return edge
            else:
                # Adding an edge between 2 vertices in different trees would merge those 2 trees.
                # i.e. every vertex with in tree v becomes a member of tree u
                for vtx in trees.keys():
                    if trees[vtx] == v_tree_ID:
                        trees[vtx] = u_tree_ID

    def findRedundantConnection_UnionFind(self, edges: List[List[int]]) -> List[int]:
        class Vertex:
            def __init__(self, id: int, treeID: int, next_vtx_in_tree: 'Vertex' = None):
                self.id = id # vertex ID
                self.treeID = treeID
                self.next_vtx_in_tree = next_vtx_in_tree

        class Tree:
            def __init__(self, head_vtx: Vertex):
                self.size = 1
                self.head_vertex = head_vtx
                self.tail_vertex = head_vtx # Initially, each tree has only 1 vertex

        # Create nodes and trees based on edges
        vertices = {}
        trees = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            if not u in vertices.keys():
                u_vtx = Vertex(u, u)
                vertices[u] = u_vtx
                trees[u] = Tree(u_vtx)
            if not v in vertices.keys():
                v_vtx = Vertex(v, v)
                vertices[v] = v_vtx
                trees[v] = Tree(v_vtx)

        # Find the edge that would create a cycle in the tree
        for edge in edges:
            u, v = edge[0], edge[1]
            if vertices[u].treeID == vertices[v].treeID:
                return edge
            else:
                u_tree = trees[vertices[u].treeID]
                v_tree = trees[vertices[v].treeID]
                # (1) Link bigger tree's tail's next to smaller tree's head
                # (2) Change bigger tree's tail to smaller tree's tail
                # (3) Change every tree whose ID is the smaller tree's ID to the bigger tree's ID
                # (4) Update size of bigger tree
                if u_tree.size >= v_tree.size:
                    # Step 1
                    u_tree.tail_vertex.next_vtx_in_tree = v_tree.head_vertex
                    # Step 2
                    u_tree.tail_vertex = v_tree.tail_vertex
                    # Step 3
                    curr_vtx = v_tree.head_vertex
                    while curr_vtx:
                        curr_vtx.treeID = u_tree.head_vertex.treeID
                        curr_vtx = curr_vtx.next_vtx_in_tree
                    # Step 4
                    u_tree.size += v_tree.size
                else:
                    # Step 1
                    v_tree.tail_vertex.next_vtx_in_tree = u_tree.head_vertex
                    # Step 2
                    v_tree.tail_vertex = u_tree.tail_vertex
                    # Step 3
                    curr_vtx = u_tree.head_vertex
                    while curr_vtx:
                        curr_vtx.treeID = v_tree.head_vertex.treeID
                        curr_vtx = curr_vtx.next_vtx_in_tree
                    # Step 4
                    v_tree.size += u_tree.size
                
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # trivial case: triangle
        if len(edges) == 3:
            return edges[-1]
        #return self.findRedundantConnection_Prim(edges)
        #return self.findRedundantConnection_Kruskal(edges)
        return self.findRedundantConnection_UnionFind(edges)