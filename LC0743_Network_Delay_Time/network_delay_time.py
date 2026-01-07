import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Construct a directed graph, where the cost of an edge is its signal travel time.
        adj = {} # maps node # to a list of its outgoing edges, denote by (target node, travel time)
        visited = {i + 1: False for i in range(n)} # denotes if a node is visited
        min_times = {i + 1: float('inf') for i in range(n)} # tracks minimum time for each node to receive the signal sent by node k
        for edge in times:
            u, v, w = edge
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((v, w))
        #print("adj:", adj)
        # Perform Dijkstra's to find the minimum time for each node to receive a signal sent by node k.
        pq = []
        heapq.heappush(pq, (0, k))
        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            if not visited[curr_node]:
                visited[curr_node] = True
                min_times[curr_node] = curr_time
                # Enqueue all the unvisited neighbors of curr_node.
                for out_edge in adj[curr_node]:
                    neighbor, cost = out_edge
                    if not visited[neighbor]:
                        heapq.heappush(pq, (min_times[curr_node] + cost, neighbor))
        #print("min_times:", min_times)
        # Scan through min_times to find the longest time it takes any one node to receive the signal.
        answer = float('-inf')
        for node, time in min_times.items():
            if time == float('inf'):
                return -1
            answer = max(answer, time)
        
        return answer
        