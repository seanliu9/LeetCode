from collections import deque
from typing import List

class Solution:
    def rDepth(self, vtx: int, adj: dict, visited: set) -> int:
        visited.add(vtx)
        if len(adj[vtx]) == 1:
            # Leaves have depth of 0
            return 0
        else:
            max_depth = -1
            for nbr in adj[vtx]:
                if nbr not in visited:
                    nbr_depth = self.rDepth(nbr, adj, visited)
                    max_depth = max(max_depth, nbr_depth)
            return max_depth + 1

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # trivial cases
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        # Construct adjacency list
        adj = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in adj.keys():
                adj[u] = [v]
            else:
                adj[u].append(v)
            if v not in adj.keys():
                adj[v] = [u]
            else:
                adj[v].append(u)
        
        # Identify leaves of the tree
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])
        
        # Remove leaves layer by layer.
        while n > 2:
            num_leaves = len(leaves)
            n -= num_leaves
            for i in range(num_leaves):
                leaf = leaves.popleft()
                for nbr in adj[leaf]:
                    adj[nbr].remove(leaf)
                    if len(adj[nbr]) == 1: # nbr becomes a leaf now
                        leaves.append(nbr)
        
        return list(leaves)