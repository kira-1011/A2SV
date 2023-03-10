# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        level_order = []
        queue = deque()
        queue.append([root, 0])
        max_width = 0

        # Level order traversal
        while queue:

            length = len(queue)
            level = []

            for i in range(length):
                
                curr_root, col = queue.popleft()

                if curr_root:
                    level.append(col)
                    queue.append([curr_root.left, 2 * col])
                    queue.append([curr_root.right, (2 * col) + 1])
            
            if level:
                # Find max width
                max_range = level[-1] - level[0] + 1
                max_width = max(max_width, max_range)
                level_order.append(level)

        return max_width
