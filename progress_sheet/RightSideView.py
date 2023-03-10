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
            
            visited = queue.popleft()

            if visited:
                level.append(visited.val)
                queue.append(visited.left)
                queue.append(visited.right)
        
        if level:
            nodes.append(level)
        
        self.BFS(root.left, queue, nodes)
        self.BFS(root.right, queue, nodes)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = deque()
        queue.append(root)
        
        nodes = []
        right_nodes = []

        self.BFS(root, queue, nodes)

        for node in nodes:
            right_nodes.append(node[-1])

        return right_nodes
