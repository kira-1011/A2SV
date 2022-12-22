class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize our left and right pointers
        left = m - 1
        right = n - 1
        i = m + n - 1

        # Start with the last elements and overwrite the empty spots
        while left >= 0 and right >= 0:

            if nums1[left] >= nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1
            
            i -= 1
        

        # Copy the remaining elements
        while left >= 0:
            nums1[i] = nums1[left]
            i -= 1
            left -= 1

        while right >= 0:
            nums1[i] = nums2[right]
            i -= 1
            right -= 1

