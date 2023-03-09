# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def traverseLevelOrder(self, root, queue):

    #     if not root:
    #         return []

    #     curr_level = []
    #     length = len(queue)

    #     for i in range(length):

    #         visited = queue.popleft()
    #         curr_level.append(visited.val)

    #         if not root.right:
    #             queue.append(root.left)
        
    #         elif not root.left:
    #             queue.append(root.right)
        
    #         else:
    #             queue.append(root.left)
    #             queue.append(root.right)
        
    #     left = self.traverseLevelOrder(root.left, queue)
    #     right = self.traverseLevelOrder(root.right, queue)

        # return [curr_level, left]        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        queue.append(root)
        level_order = []

        while queue:

            length = len(queue)
            level = []
            
            for i in range(length):
                visited = queue.popleft()
                    
                if visited:
                    level.append(visited.val)
                    queue.append(visited.left)
                    queue.append(visited.right)
            
            if level:
                level_order.append(level)

        return level_order
    
