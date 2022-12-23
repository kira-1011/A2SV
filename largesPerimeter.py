class Solution:
    def checkValidity(self, side1, side2, side3):
        if side2 + side3 > side1:
            return True
        return False

    def largestPerimeter(self, nums: List[int]) -> int:
        large_perimeter = 0
        n = len(nums)

        # Sort the length of the sides
        nums.sort()

        # Check validity of the sides and track the maximum perimeter if it is valid
        for i in range(n - 1, 1, -1):
            side1 = nums[i]
            side2 = nums[i - 1]
            side3 = nums[i - 2]
            valid = self.checkValidity(side1, side2, side3)

            if valid == True:
                perimeter = side1 + side2 + side3
                large_perimeter = max(large_perimeter, perimeter)

        return large_perimeter