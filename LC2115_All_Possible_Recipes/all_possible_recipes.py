from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.clock = 1
        self.ordering = {} # maps node to its [preorder, postorder]
        self.topo_order = deque()
        self.supplies_set = set()
        self.recipes_set = set()

    # ordering is a dictionary that maps a vertex to its [preorder, postorder]
    def topo_sort(self, start_vtx: str, adj: dict):
        # if start_vtx has already been visited
        if self.ordering[start_vtx][0] != 0:
            return

        # Set preorder of start_vtx
        self.ordering[start_vtx][0] = self.clock
        self.clock += 1

        # Perform DFS on all the outgoing vertices of start_vtx.
        for nbr in adj[start_vtx]:
            if nbr in self.supplies_set or nbr in self.recipes_set:
                if self.ordering[nbr][1] == 0: # if the vertex hasn't been fully processed yet
                    self.topo_sort(nbr, adj)

        self.ordering[start_vtx][1] = self.clock
        self.clock += 1
        self.topo_order.append(start_vtx)

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Construct a directed adjacency list with nodes as recipe items and supplies.
        # An edge from u to v means that u takes v as an input.
        self.supplies_set = set(supplies)
        self.recipes_set = set(recipes)
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
        self.ordering = {node: [0, 0] for node in adj.keys()} # maps node to its [preorder, postorder]
        for node in adj.keys():
            if self.ordering[node][0] == 0: # if this node hasn't been visited yet
                self.topo_sort(node, adj)

        # For each recipe, determine if it is makeable, starting from the rightmost to the leftmost recipe.
        # print("ordering:")
        # for k, v in self.ordering.items():
        #     print(f"k = {k}, v = {v}")
        topo_order = list(self.topo_order)[::-1]
        #print(topo_order)
        answer = []
        for item in reversed(topo_order):
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
    
if __name__ == "__main__":
    solution = Solution()
    recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
    ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
    supplies = ["wi","otr","wbjr","fzr","xgp"]
    solution.findAllRecipes(recipes, ingredients, supplies)

        