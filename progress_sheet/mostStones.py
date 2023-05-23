class UnionFind():

    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.size = {i : 1 for i in range(n)}
    
    def find(self, x):

        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):

        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep == y_rep:
            return False
        
        if self.size[x_rep] > self.size[y_rep]:
            self.parent[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]
        
        elif self.size[y_rep] < self.size[x_rep]:
            self.parent[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]
        
        else:
            self.parent[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        union_find = UnionFind(len(stones))
        none_removed = 0

        # check stones with equal rows and cols
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):

                x1, y1 = stones[i]
                x2, y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    union_find.union(i, j)

        for i in range(len(stones)):
            
           if union_find.find(i) == i:
               none_removed += 1

        return len(stones) - none_removed
