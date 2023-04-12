# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.root_to_leaf = [0]

    def dfs(self, root, path):

        if not root:
            return
        
        path.append(str(root.val))
        
        if not root.left and not root.right:
            
            num = int(''.join(path.copy()))

            self.root_to_leaf.append(num)

        self.dfs(root.left, path)
        self.dfs(root.right, path)

        path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.dfs(root, [])

        return sum(self.root_to_leaf)
