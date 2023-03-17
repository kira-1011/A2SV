# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.max_sum = float('-inf')

    def findMaxSum(self, root):

        if not root:
            return 0

        left_max = self.findMaxSum(root.left)
        right_max = self.findMaxSum(root.right)
        mid_max = left_max + right_max + root.val

        self.max_sum = max(self.max_sum, left_max + root.val, mid_max, right_max + root.val, root.val)

        return max(left_max + root.val, right_max + root.val, root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.findMaxSum(root)

        return self.max_sum
