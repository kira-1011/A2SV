class UnionFind:

    def __init__(self, size):
        self.parent = {i : i for i in range(size)}
        self.height = {i : 0 for i in range(size)}
    
    def find(self, node):
        
        # Applying path comprehension to optimize quick find
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return self.parent[node]
    
    def union(self, node1, node2):
        
        # Union by height(rank)
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)

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
    
    def isConnected(self, node1, node2):
        return  self.find(node1) == self.find(node2)


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        union_find = UnionFind(n)

        for node1, node2 in edges:
            union_find.union(node1, node2)

        return union_find.isConnected(source, destination)
