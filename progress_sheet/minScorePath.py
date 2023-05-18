class UnionFind:

    def __init__(self, size):
        self.parent = {i : i for i in range(size)}
        self.rank = {i : i for i in range(size)}
        self.min_edge = [inf for _ in range(size)]
    
    def find(self, node):

        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1, node2, distance):

        rep1 = self.find(node1)
        rep2 = self.find(node2)

        if rep1 == rep2:
            self.min_edge[rep1] = min(self.min_edge[rep1], self.min_edge[rep2], distance)
            return False

        if self.rank[rep1] > self.rank[rep2]:
            self.parent[rep2] = rep1
            self.min_edge[rep1] = min(self.min_edge[rep1], self.min_edge[rep2], distance)
        
        elif self.rank[rep2] > self.rank[rep1]:
            self.parent[rep1] = rep2
            self.min_edge[rep2] = min(self.min_edge[rep1], self.min_edge[rep2], distance)
        
        else:
            self.parent[rep2] = rep1
            self.rank[rep1] += 1
            self.min_edge[rep1] = min(self.min_edge[rep1], self.min_edge[rep2], distance)
        
        return True
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)
    
    def getMinEdge(self, n):
        return self.min_edge[self.find(0)]

class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        union_find = UnionFind(n)

        for node1, node2, distance in roads:
            union_find.union(node1 - 1, node2 - 1, distance)

        return union_find.getMinEdge(n - 1)
