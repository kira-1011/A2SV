class Solution:

    def __init__(self):
        self.smaller_count = []

    def mergeSort(self, nums, left, right):

        if left >= right:
            return [nums[left]]
        
        mid = left + (right - left) // 2

        left_half = self.mergeSort(nums, left, mid)
        right_half = self.mergeSort(nums, mid + 1, right)

        # Count smaller numbers for each element in the left
        r_ptr = 0

        for l_ptr in range(len(left_half)):

            while r_ptr < len(right_half) and left_half[l_ptr][0] > right_half[r_ptr][0]:
                r_ptr += 1

            self.smaller_count[left_half[l_ptr][1]] += r_ptr
        
        # Sort and merge
        merged = []
        l_ptr = 0
        r_ptr = 0
        left_len = len(left_half)
        right_len = len(right_half)

        while l_ptr < left_len and r_ptr < right_len:

            if left_half[l_ptr][0] <= right_half[r_ptr][0]:
                merged.append(left_half[l_ptr])
                l_ptr += 1

            else:
                merged.append(right_half[r_ptr])
                r_ptr += 1
        
        while l_ptr < len(left_half):
            merged.append(left_half[l_ptr])
            l_ptr += 1
        
        while r_ptr < right_len:
            merged.append(right_half[r_ptr])
            r_ptr += 1

        return merged
        
    def countSmaller(self, nums: List[int]) -> List[int]:

        indices = [i for i in range(len(nums))]

        nums = list(zip(nums, indices))
        self.smaller_count = [0] * len(nums)

        self.mergeSort(nums, 0, len(nums) - 1)

        return self.smaller_count
