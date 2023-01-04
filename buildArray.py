class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        nums_size = len(nums)
        answer = [0] * nums_size

        for i in nums:
            answer[i] = nums[nums[i]]

        return answer