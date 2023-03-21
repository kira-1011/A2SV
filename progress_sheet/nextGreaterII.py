class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        mono_stack = []
        next_greater = [-1 for i in range(len(nums))]

        length = len(nums)
        
        # append the whole array again to traverse in circle 
        nums.extend(nums)

        for i in range(len(nums)):

            while mono_stack and nums[mono_stack[-1]] < nums[i]:

                # use modulo to calculate the offset from the start of the array
                next_greater[mono_stack.pop() % length] = nums[i]
            
            mono_stack.append(i)

        return next_greater
