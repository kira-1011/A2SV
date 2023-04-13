# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.even_sum = 0 

    def dfs(self, path, grand, curr, root):

        if not root:
            return
        
        path.append(root.val)
        
        if grand > -1 and path[grand] % 2 == 0:
            self.even_sum += path[curr]

        self.dfs(path, grand + 1, curr + 1, root.left)
        self.dfs(path, grand + 1, curr + 1, root.right)

        path.pop()

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.dfs([], -2, 0, root)

        return self.even_sum
