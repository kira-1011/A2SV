class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        mono_stack = []
        min_val = nums[0]

        # while maintaining only the 32 pattern look for the 1 pattern  
        for num in nums:

            while mono_stack and mono_stack[-1][0] <= num:
                mono_stack.pop()

            if mono_stack and num > mono_stack[-1][1]:
                return True

            mono_stack.append((num, min_val))
            min_val = min(min_val, num)

        return False
