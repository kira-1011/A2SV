# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.sumOfTilt = 0

    def findTiltSum(self, root):

        if not root:
            return 0
        
        left_val = self.findTiltSum(root.left)
        right_val = self.findTiltSum(root.right)

        self.sumOfTilt += (abs(left_val - right_val))

        return left_val + root.val + right_val

    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.findTiltSum(root)

        return self.sumOfTilt
