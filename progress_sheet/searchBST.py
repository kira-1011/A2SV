# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root == None:
            return
        
        # if we found our value return the subtree
        if root.val == val:
            return root
        
        # if the target is greater than the current node traverse to the right
        if val > root.val:
            return self.searchBST(root.right, val)
        
        if val < root.val:
            # otherwise traverse to the left
            return self.searchBST(root.left, val)
