# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.solution = []

    def findPath(self, root, path):

        if not root:
            return
        
        path.append(str(root.val))

        self.findPath(root.left, path)

        self.findPath(root.right, path)
        
        if not root.left and not root.right:
            self.solution.append('->'.join(path))

        path.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.findPath(root, [])

        return self.solution
