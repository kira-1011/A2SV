# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def createBst(self, preorder):

        if not preorder:
            return None

        node = TreeNode(preorder[0])
        bisect_pos = 1
 
        while bisect_pos < len(preorder) and preorder[bisect_pos] < node.val:
            bisect_pos+=1

        node.left = self.bstFromPreorder(preorder[1 :bisect_pos])
        node.right = self.bstFromPreorder(preorder[bisect_pos : ])

        return node

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        return self.createBst(preorder)
