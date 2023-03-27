class Solution:

    def __init__(self):
        self.pair_count = 0
        self.diff = 0

    def mergeSort(self, merged_diff, left, right):

        if left == right:
            return [merged_diff[left]]
        
        mid = left + (right - left) // 2

        left_half = self.mergeSort(merged_diff, left, mid)
        right_half = self.mergeSort(merged_diff, mid + 1, right)

        # Search for pairs that satisfy the condition
        for j in range(len(right_half)):
            target = right_half[j] + self.diff
            pos = bisect_right(left_half, target)
            self.pair_count += (pos)

        # Sort and merge
        merged = []
        left_ptr = 0
        right_ptr = 0
        left_len = len(left_half)

        while left_ptr < left_len and right_ptr < len(right_half):

            if left_half[left_ptr] <= right_half[right_ptr]:
                merged.append(left_half[left_ptr])
                left_ptr += 1

            else:
                merged.append(right_half[right_ptr])
                right_ptr += 1
        
        while left_ptr < len(left_half):
            merged.append(left_half[left_ptr])
            left_ptr += 1
        
        while right_ptr < len(right_half):
            merged.append(right_half[right_ptr])
            right_ptr += 1

        return merged

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        size = len(nums1)
        merged_diff = [0] * size
        self.diff = diff

        # Calculate merged difference
        for i in range(size):
            merged_diff[i] = nums1[i] - nums2[i]
        
        # Count number of pairs by dividing and sorting back(merge sort)
        self.mergeSort(merged_diff, 0, size - 1)

        return self.pair_count
