# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def BFS(self, root, queue, nodes):

        if not root:
            return
        
        if not queue:
            return
        
        length = len(queue)
        level = []

        for i in range(length):
            
            curr_root, col = queue.popleft()

            if curr_root:
                level.append(col)
                queue.append([curr_root.left, 2 * col])
                queue.append([curr_root.right, (2 * col) + 1])
        
        if level:
            nodes.append(level)
        
        self.BFS(root.left, queue, nodes)
        self.BFS(root.right, queue, nodes)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        level_order = []
        queue = deque()
        queue.append([root, 0])

        self.BFS(root, queue, level_order)
        
        max_width = 0

        for level in level_order:
            max_range = level[-1] - level[0] + 1
            max_width = max(max_width, max_range)

        return max_width
