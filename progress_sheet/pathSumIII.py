# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        
        self.total_count = 0
        self.targetSum = 0

    def findPathSum(self, root, prefix_sum, prefix_count):

        if not root:
            return


        prefix_sum += root.val

        if prefix_sum == self.targetSum:
            self.total_count += 1

        self.total_count += (prefix_count[(prefix_sum - self.targetSum)])

        prefix_count[prefix_sum] += 1
        
        # traverse left
        self.findPathSum(root.left, prefix_sum, prefix_count)

        # traverse right
        self.findPathSum(root.right, prefix_sum, prefix_count)

        prefix_count[prefix_sum] -= 1
        prefix_sum -= root.val


        return

    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.targetSum = targetSum

        prefix_count = defaultdict(int)
        prefix_sum = 0

        self.findPathSum(root, prefix_sum, prefix_count)
        
        return self.total_count
