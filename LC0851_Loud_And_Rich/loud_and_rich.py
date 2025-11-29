from typing import List

class Solution:
    def rHeight(self, node: int, adj: dict, heights: dict, nodes_by_height: dict) -> int:
        if node in heights:
            return heights[node]

        if adj[node] == []: 
            # if node is a leaf
            heights[node] = 0
            nodes_by_height[0].append(node)
            return 0
        else:
            max_height_of_children = -1
            for child in adj[node]:
                max_height_of_children = max(max_height_of_children, self.rHeight(child, adj, heights, nodes_by_height))
            heights[node] = max_height_of_children + 1
            nodes_by_height[max_height_of_children + 1].append(node)
            return max_height_of_children + 1

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet) # number of people
        # trivial cases
        if n == 0:
            return []
        elif n == 1:
            return [0]

        # Construct a directed adjacency list representation of richer.
        # An edge from u to v means that v is richer than u.
        adj = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}
        for a, b in richer:
            adj[b].append(a)
            in_degree[a] += 1

        # Create a super source (with ID n) that points to every node that has no incoming edges.
        # Note that we don't have to worry about cycles, because we are told that are the data is logically consistent.
        adj[n] = []
        for i in range(n):
            if in_degree[i] == 0:
                adj[n].append(i)

        # Calculate the height of each node in the graph. Each leaf has height 0.
        nodes_by_height = {i: [] for i in range(n + 1)}
        heights = {}
        max_height = self.rHeight(n, adj, heights, nodes_by_height)

        answer = [-1] * n
        # DP- start with the leaves (whose height = 0) and answer[leaf] = leaf
        for height, nodes in nodes_by_height.items():
            if height == 0: 
                # base case
                for node in nodes:
                    answer[node] = node
            elif height < max_height:
                # recurrence
                for node in nodes:
                    # Consider node and each answer[children] for each of its children
                    x = node
                    min_quietness = quiet[node]
                    for child in adj[node]:
                        if quiet[answer[child]] < min_quietness:
                            min_quietness = quiet[answer[child]]
                            x = answer[child]
                    answer[node] = x
            else:
                break
            #print(f"after iteration {height}, answer = {answer}")
        return answer