# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraverse(self, root, freq_count):
        
        if not root:
            return
        
        self.inorderTraverse(root.left, freq_count)
        freq_count[root.val] += 1
        self.inorderTraverse(root.right, freq_count)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        freq_count = defaultdict(int)
        modes = []
        max_freq = 0

        # Traverse tree inorder and count the nodes frequency
        self.inorderTraverse(root, freq_count)

        # Find the maximum frequency
        max_freq = max(freq_count.values())

        # find nodes with the maximum frequency i.e modes
        for key in freq_count.keys():
            if freq_count[key] == max_freq:
                modes.append(key)

        return modes
