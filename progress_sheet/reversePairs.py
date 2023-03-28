class Solution:

    def __init__(self):
        self.pairs = 0

    def mergeSort(self,nums, left, right):

        if left == right:
            return [nums[left]]
        
        mid = left + (right - left) // 2
        left_half = self.mergeSort(nums, left, mid)
        right_half = self.mergeSort(nums, mid + 1, right)

        # count the number of pairs satisfying the condition
        for j in range(len(right_half)):
            pos = bisect_right(left_half, right_half[j] * 2)
            self.pairs += (len(left_half) - pos)

        # Sort and merge
        merged = []
        left_ptr = 0
        right_ptr = 0
        left_len = len(left_half)
        right_len = len(right_half)

        while left_ptr < left_len and right_ptr < right_len:

            if left_half[left_ptr] <= right_half[right_ptr]:
                merged.append(left_half[left_ptr])
                left_ptr += 1

            else:
                merged.append(right_half[right_ptr])
                right_ptr += 1
        
        while left_ptr < len(left_half):
            merged.append(left_half[left_ptr])
            left_ptr += 1
        
        while right_ptr < right_len:
            merged.append(right_half[right_ptr])
            right_ptr += 1
        
        return merged

        
    def reversePairs(self, nums: List[int]) -> int:

        self.mergeSort(nums, 0, len(nums) - 1)

        return self.pairs

        
