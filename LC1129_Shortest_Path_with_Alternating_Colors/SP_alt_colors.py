from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)} # maps node ID to list of nodes that it's adjacent to
        
        # A red edge is from a blue node to a red node.
        for u, v in redEdges:
            adj[u].append((v, "red"))
        # A blue edge is from a red node to a blue node.
        for u, v in blueEdges:
            adj[u].append((v, "blue"))
        
        # Perform BFS to compute shortest path distance arrays for each color
        dist_red = [-1] * n 
        dist_blue = [-1] * n
        
        q = deque()
        dist_red[0] = 0
        dist_blue[0] = 0
        q.append((0, "red", 0)) 
        q.append((0, "blue", 0))

        while q:
            curr_node, curr_color, curr_dist = q.popleft()
            # Visit the unvisited adjacent nodes with the opposite edge color.
            # Note that if a node's value in a distance array is -1, it hasn't been visited yet.
            for neighbor, edge_color in adj[curr_node]:
                if curr_color == "red" and edge_color == "blue" and dist_blue[neighbor] == -1:
                    dist_blue[neighbor] = curr_dist + 1
                    q.append((neighbor, "blue", curr_dist + 1))
                elif curr_color == "blue" and edge_color == "red" and dist_red[neighbor] == -1:
                    dist_red[neighbor] = curr_dist + 1
                    q.append((neighbor, "red", curr_dist + 1))
        
        result = [-1] * n
        for i in range(n):
            # The shortest path for node i is the minimum of the distances found
            if dist_red[i] == -1 and dist_blue[i] == -1:
                # if node i is unreachable from either the red or blue source
                result[i] = -1
            elif dist_red[i] == -1:
                # if node i is is only reachable from the blue source
                result[i] = dist_blue[i]
            elif dist_blue[i] == -1:
                # if node i is only reachable from the red source
                result[i] = dist_red[i]
            else:
                # if node i is reachable from both the red and the blue source
                result[i] = min(dist_red[i], dist_blue[i])
        
        return result
