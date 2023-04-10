"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def __init__(self):
        self.max_depth = 0

    def dfs(self, node, visited, curr_depth):

        self.max_depth = max(self.max_depth, curr_depth)

        visited.add(node)

        for child in node.children:

            if child not in visited:
                self.dfs(child, visited, curr_depth + 1)
            

    def maxDepth(self, root: 'Node') -> int:

        self.max_depth = 0

        self.dfs(root, set(), 1)

        return self.max_depth
