# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self, root):

        if not root:
            return ''
        
        left_str = self.preorder(root.left)
        right_str = self.preorder(root.right)

        curr_str = [str(root.val)]

        if root.left and not root.right:
            return str(root.val) + '(' + left_str + ')'
        
        if not root.left and not root.right:
            return str(root.val)

        return str(root.val) + '(' + left_str + ')' + '(' + right_str + ')'

    def tree2str(self, root: Optional[TreeNode]) -> str:

        return self.preorder(root)
