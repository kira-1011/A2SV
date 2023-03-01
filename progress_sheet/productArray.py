class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)
        left_product = [1] * (size + 1)
        right_product = [1] * (size + 1)
        nums.append(1)

        # Store left prefix product
        for i in range(size):
            left_product[i] = left_cproduct[i - 1] * nums[i]
        
        # Store right prefix product
        for i in range(size - 1, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i]

        # multiply left product and right product excluding the current element
        for i in range(size):
            nums[i] = right_product[i + 1] * left_product[i - 1]
        
        nums.pop()

        return nums
