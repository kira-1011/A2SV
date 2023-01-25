class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        placeholder = 0
        seeker = 0
        size = len(nums)

        # Remove duplicates using two pointers
        while seeker < size:

            if nums[placeholder] != nums[seeker]:
                nums[placeholder + 1], nums[seeker] = nums[seeker], nums[placeholder + 1]
                placeholder += 1
            
            seeker += 1
        
        k = placeholder + 1

        return k