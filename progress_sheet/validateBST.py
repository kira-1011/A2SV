# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def validate(self, root, lower, upper):

        if not root:
            return True

        if not (lower < root.val < upper):
            return False
        
        left_tree = self.validate(root.left, lower, root.val)
        right_tree = self.validate(root.right, root.val, upper)

        return left_tree and right_tree

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.validate(root, float('-inf'), float('inf'))
