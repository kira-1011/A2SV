class Solution:

    def reverseInt(self, num):

        rev_int = 0

        while num:

            last = num % 10
            num //= 10
            rev_int = rev_int * 10 + last
        
        return rev_int

    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums.append(self.reverseInt(nums[i]))

        return len(set(nums))
