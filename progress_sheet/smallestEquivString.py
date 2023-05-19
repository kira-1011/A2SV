class UnionFind:

    def __init__(self):
        self.parent = {chr(ord('a') + i) : chr(ord('a') + i) for i in range(26)}
    
    def find(self, node):

        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1, node2):

        rep1 = self.find(node1)
        rep2 = self.find(node2)

        if rep1 == rep2:
            return False

        # Make the reperesenatitve the one with smaller lexicographical order
        if rep1 > rep2:
            self.parent[rep1] = rep2
        
        else:
            self.parent[rep2] = rep1
        
        return True
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)
    

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        union_find = UnionFind()
        equiv_str = []

        for i in range(len(s1)):
            union_find.union(s1[i], s2[i])
        
        for char in baseStr:
            equiv_str.append(union_find.find(char))
        
        return ''.join(equiv_str)
