class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]

        pivot = -1
        size = len(nums)
        left = 0
        right = size - 1

        while pivot != size - k:
            
            write = left + 1
            pivot = left

            for read in range(left + 1, right + 1):

                if nums[read] <= nums[pivot]:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
                
            nums[pivot], nums[write - 1] = nums[write - 1], nums[pivot]
            pivot = write - 1

            if pivot < size - k:
                left = pivot + 1

            elif pivot > size - k:
                right = pivot - 1
        
        return nums[pivot]
