# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findAvg(self, root):

        if not root:
            return 0,0,0
        
        left_sum, left_nodes, left_count = self.findAvg(root.left)
        right_sum, right_nodes, right_count = self.findAvg(root.right)

        total_sum = left_sum + right_sum + root.val
        total_nodes = left_nodes + right_nodes + 1
        total_count = left_count + right_count

        avg = total_sum // total_nodes

        if avg == root.val:
            total_count += 1
        
        return total_sum, total_nodes, total_count

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        _sum, nodes, count = self.findAvg(root)

        return count
