# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.sum_count = defaultdict(int)

    def findTreeSum(self, root):

        if not root:
            return 0

        left_sum = self.findTreeSum(root.left)
        right_sum = self.findTreeSum(root.right)

        total = left_sum + right_sum + root.val
        self.sum_count[total] += 1

        return total

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        self.findTreeSum(root)
        max_freq = max(self.sum_count.values())
        freq_sum = []

        for count in self.sum_count:
            
            if self.sum_count[count] == max_freq:
                freq_sum.append(count)
        
        return freq_sum
