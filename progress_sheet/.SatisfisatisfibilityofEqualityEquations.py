class UnionFind:

    def __init__(self):
        self.parent = {chr(ord('a') + i) : chr(ord('a') + i) for i in range(26)}
        self.rank = {chr(ord('a') + i) : 0 for i in range(26)}
    
    def find(self, node):
        
        # Applying path comprehension to optimize quick find
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1, node2):
        
        # Union by rank(rank)
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)

        if node1_rep == node2_rep:
            return False

        if self.rank[node1_rep] > self.rank[node2_rep]:
            self.parent[node2_rep] = node1_rep
        
        elif self.rank[node1_rep] < self.rank[node2_rep]:
            self.parent[node1_rep] = node2_rep

        else:
            self.parent[node2_rep] = node1_rep
            self.rank[node1_rep] += 1

        return True

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        union_find = UnionFind()
        for equation in equations:
            l_op, op, r_op = equation[0 : 1], equation[1 : 3], equation[3 : ]

            if op == "==":
                union_find.union(l_op, r_op)
        
        for equation in equations:
            l_op, op, r_op = equation[0 : 1], equation[1 : 3], equation[3 : ]

            if op == "!=" and  union_find.isConnected(l_op, r_op):
                return False
        
        return True
