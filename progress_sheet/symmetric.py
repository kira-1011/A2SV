# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def validate(self, root1, root2):

        # If we completed the tree in both directions return true
        if not root1 and not root2:
            return True
        
        # if one of the nodes are null or their values are not equal return true
        if (not root1 and root2) or (not root2 and root1) or (root1.val != root2.val):
            return False
        
        # Check our left subtree and right subtree
        left = self.validate(root1.left, root2.right)
        right = self.validate(root1.right, root2.left)

        return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        return self.validate(root.left, root.right)
