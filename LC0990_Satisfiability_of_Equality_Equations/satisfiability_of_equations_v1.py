from typing import List

class Vertex:
    def __init__(self, id: str, component_id: str):
        self.id = id
        self.component_id = component_id
        self.next_vtx_in_component = None

class Component:
    def __init__(self, head_vtx: Vertex):
        self.size = 1
        self.head_vtx = head_vtx
        self.tail_vtx = head_vtx # Initially, each component only has 1 vertex.

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Parse the equations to construct the graph.
        vertices = {} # maps string to Vertex object
        components = {} # maps string to Component object
        for equation in equations:
            u, v = equation[0], equation[3]
            if u not in vertices.keys():
                u_vtx = Vertex(u, u)
                vertices[u] = u_vtx
                components[u] = Component(u_vtx)
            if v not in vertices.keys():
                v_vtx = Vertex(v, v)
                vertices[v] = v_vtx
                components[v] = Component(v_vtx)
        
        # Perform union find on all the equalities.
        for equation in equations:
            if equation[1] == '=':
                u, v = equation[0], equation[3]
                u_vtx = vertices[u]
                v_vtx = vertices[v]
                if u_vtx.component_id != v_vtx.component_id:
                    u_comp = components[u_vtx.component_id]
                    v_comp = components[v_vtx.component_id]
                    # (1) Link bigger component's tail's next pointer to smaller component's head
                    # (2) Change bigger component's tail to smaller component's tail
                    # (3) Change every component whose ID is the smaller component's ID to the bigger component's ID
                    # (4) Update size of bigger component
                    if u_comp.size >= v_comp.size:
                        # Step 1
                        u_comp.tail_vtx.next_vtx_in_component = v_comp.head_vtx
                        # Step 2
                        u_comp.tail_vtx = v_comp.tail_vtx
                        # Step 3
                        curr_vtx = v_comp.head_vtx
                        while curr_vtx:
                            curr_vtx.component_id = u_comp.head_vtx.component_id
                            curr_vtx = curr_vtx.next_vtx_in_component
                        # Step 4
                        u_comp.size += v_comp.size
                    else:
                        # Step 1
                        v_comp.tail_vtx.next_vtx_in_component = u_comp.head_vtx
                        # Step 2
                        v_comp.tail_vtx = u_comp.tail_vtx
                        # Step 3
                        curr_vtx = u_comp.head_vtx
                        while curr_vtx:
                            curr_vtx.component_id = v_comp.head_vtx.component_id
                            curr_vtx = curr_vtx.next_vtx_in_component
                        # Step 4
                        v_comp.size += u_comp.size

        # For each inequality, check if the two variables belong to the same component. If so, immediately return False.
        for equation in equations:
            if equation[1] == "!":
                u, v = equation[0], equation[3]
                if vertices[u].component_id == vertices[v].component_id:
                    return False
        
        return True
                    
            
