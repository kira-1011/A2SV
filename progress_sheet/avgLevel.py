# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfsAverage(self, root):

        queue = deque([root])
        avg = []
        
        while queue:

            level_len = len(queue)
            curr_sum = 0

            for i in range(level_len):

                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            avg.append(curr_sum / level_len)
        
        return avg

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        return self.bfsAverage(root)
