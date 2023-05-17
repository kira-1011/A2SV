class UnionFind:

    def __init__(self, size):
        self.parent = {i : i for i in range(1, size + 1)}
        self.height = {i : 0 for i in range(1, size + 1)}
    
    def quickFind(self, node):
        
        # Applying path comprehension to optimize quick find
        if node == self.parent[node]:
            return node

        self.parent[node] = self.quickFind(self.parent[node])

        return self.parent[node]
    
    def quickUnion(self, node1, node2):
        
        # Union by height(rank)
        node1_rep = self.quickFind(node1)
        node2_rep = self.quickFind(node2)

        if node1_rep == node2_rep:
            return False

        if self.height[node1_rep] > self.height[node2_rep]:
            self.parent[node2_rep] = node1_rep
        
        elif self.height[node1_rep] < self.height[node2_rep]:
            self.parent[node1_rep] = node2_rep

        else:
            self.parent[node2_rep] = node1_rep
            self.height[node1_rep] += 1

        return True

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        union_find = UnionFind(len(edges))

        for node1, node2 in edges:
            
            if not union_find.quickUnion(node1, node2):
                return [node1, node2]
        
