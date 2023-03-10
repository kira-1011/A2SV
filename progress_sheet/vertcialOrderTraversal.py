# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root, row, col):

        if not root:
            return []
        
        left = self.inorderTraversal(root.left, row + 1, col - 1)
        right = self.inorderTraversal(root.right, row + 1, col + 1)

        return left + [[col, row, root.val]] + right

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = self.inorderTraversal(root, 0, 0)

        cols = set()

        for node in nodes:
            cols.add(node[0])

        min_col = min(cols)
        max_col = max(cols)
        
        nodes.sort()
        
        answer = [[] for i in range(len(cols))]

        for node in nodes:
            answer[node[0] - min_col].append(node[2])

        return answer
