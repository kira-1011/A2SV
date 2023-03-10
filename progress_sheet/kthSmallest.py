# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraverse(self, root):

        if not root:
            return []
        
        left_tree = self.inorderTraverse(root.left)
        right_tree = self.inorderTraverse(root.right)

        return left_tree + [root.val] + right_tree

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        nodes = self.inorderTraverse(root)

        return nodes[k - 1]
