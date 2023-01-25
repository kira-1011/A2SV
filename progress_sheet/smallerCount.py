class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        smaller_count = {}
        size = len(nums)
        sorted_arr = sorted(nums)
        answer = []

        for index in range(size):
            if sorted_arr[index] not in smaller_count:
                smaller_count[sorted_arr[index]] = index

        for num in nums:
            answer.append(smaller_count[num])

        return answer