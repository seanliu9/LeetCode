from collections import deque
from typing import List

class Solution:
    # ordering is a dictionary that maps a vertex to its [preorder, postorder]
    def topo_sort(self, start_vtx: str, adj: dict, ordering: dict, clock: int, topo_order: deque, supplies_set: set) -> int:
        if ordering[start_vtx][0] != 0:
            return -1

        # Set preorder of start_vtx
        ordering[start_vtx][0] = clock
        clock += 1

        # Perform DFS on all the outgoing vertices of start_vtx.
        for nbr in adj[start_vtx]:
            if nbr in supplies_set:
                if ordering[nbr][1] == 0:
                    clock = self.topo_sort(nbr, adj, ordering, clock, topo_order, supplies_set)
                    if clock == -1:
                        return -1

        ordering[start_vtx][1] = clock
        clock += 1
        topo_order.append(start_vtx)
        return clock

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Construct a directed adjacency list with nodes as recipe items and supplies.
        # An edge from u to v means that u takes v as an input.
        supplies_set = set(supplies)
        adj = {}
        makeable = {} # maps recipe to if it can be made or supply to if it exists- initially we don't know if a recipe is makeable
        for i in range(len(recipes)):
            makeable[recipes[i]] = False
            adj[recipes[i]] = []
            for ingredient in ingredients[i]:
                adj[recipes[i]].append(ingredient)
                makeable[ingredient] = False
        # Every supply in supplies already exists.
        for supply in supplies:
            adj[supply] = [] 
            makeable[supply] = True
        
        # Perform a topological sort on the graph
        ordering = {node: [0, 0] for node in adj.keys()} # maps node to its [preorder, postorder]
        clock = 1
        visited = {node: 0 for node in adj.keys()} 
        topo_order = deque()
        for node in adj.keys():
            if visited[node] == 0: # if this node hasn't been visited yet
                clock = self.topo_sort(node, adj, ordering, clock, topo_order, supplies_set)
        #print(ordering)
        #print(topo_order)
        # For each recipe, determine if it is makeable, starting from the rightmost to the leftmost recipe.
        topo_order = list(topo_order)
        #print(topo_order)
        answer = []
        for item in topo_order:
            if len(adj[item]) > 0:
                flag = True
                # Examine each dependency of item and determine if it's makeable
                for dependency in adj[item]:
                    if not makeable[dependency]:
                        makeable[item] = False
                        flag = False
                        break
                if flag:
                    makeable[item] = True
                    answer.append(item)
        return answer
        