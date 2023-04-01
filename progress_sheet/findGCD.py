class Solution:

    def GCD(self, num1, num2):

        if num2 == 0:
            return num1
        
        return self.GCD(num2, num1 % num2)
        
    def findGCD(self, nums: List[int]) -> int:

        num1 = min(nums)
        num2 = max(nums)

        return (self.GCD(num1, num2)) 
