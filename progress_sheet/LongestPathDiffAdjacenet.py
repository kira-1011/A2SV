class Solution:

    def __init__(self):
        self.s = ""
        self.longest = 0

    def dfs(self, tree, node):

        longest1 = 0
        longest2 = 0
      
        for next_node in tree[node]:
            
            curr_longest = self.dfs(tree, next_node)

            if self.s[node] == self.s[next_node]:
                continue

            # maintain the first most longest path and the second most longest path
            if curr_longest > longest1:
                longest2 = longest1
                longest1 = curr_longest
            
            elif curr_longest > longest2:
                longest2 = curr_longest

        # find the longest between the path formed from the first longest + second longest + current element 
        self.longest = max(self.longest, longest1 + longest2 + 1)

        # return the longest linear path with the current element added 
        return longest1 + 1

    def longestPath(self, parent: List[int], s: str) -> int:
        
        tree = defaultdict(list)
        self.s = s

        # construct the tree
        for i in range(len(parent)):

            if parent[i] == -1:
                continue

            tree[parent[i]].append(i)

        self.dfs(tree, 0)
        
        return self.longest
