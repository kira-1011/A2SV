class Solution:

    def __init__(self):
        self.solution = set()
        self.nums = []
    
    def findSubsec(self, idx, subseq):

        if len(subseq) >= 2:

            if subseq[-2] > subseq[-1] or tuple(subseq) in self.solution:
                return

            self.solution.add(tuple(subseq.copy()))
            
        # Check if current the subsequence is in non decreasing order
        for i in range(idx, len(self.nums)):

            subseq.append(self.nums[i])
            self.findSubsec(i + 1, subseq)
            subseq.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        self.nums = nums

        self.findSubsec(0, [])

        return self.solution
