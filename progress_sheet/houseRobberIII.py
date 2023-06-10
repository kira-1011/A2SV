# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.memo = dict()
    
    def choose(self, root, prev):

        if root:

            # left
            choose_left = 0

            if not prev:
                choose_left = root.val + self.dp(root.left, True)

            skip_left = self.dp(root.left, False)

            # right
            choose_right = 0

            if not prev:
                choose_right = self.dp(root.right, True)

            skip_right = self.dp(root.right, False)

            return max(choose_left + choose_right, skip_left + skip_right)
        
        return 0
        
    def dp(self, root, prev):

        if (root, prev) not in self.memo:
            self.memo[(root, prev)] = self.choose(root, prev)

        return self.memo[(root, prev)]

    def rob(self, root: Optional[TreeNode]) -> int:

        return self.dp(root, False)
