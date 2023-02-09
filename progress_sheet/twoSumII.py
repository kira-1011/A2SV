class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        # start from left most and right most 
        # and conitnue checking sum until target is found
        while left < right:
            
            sumI = numbers[left] + numbers[right]

            if sumI == target:
                return [left + 1, right + 1]
            
            if sumI > target:
                right -= 1
            else:
                left += 1
