class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        arr.append( float("-inf") )
        mono_stack = []
        min_sum = 0

        # Finding the range in which the current element is minimum
        for i in range(len(arr)):
            
            while mono_stack and arr[mono_stack[-1]] >= arr[i]:
                
                # find the right boundary at which the current element is minimum
                mid = mono_stack.pop()
                right = i - mid

                # find the left boundary at which the current element is minimum
                left = mid + 1

                if mono_stack:
                    left = mid - mono_stack[-1]

                # Calc the total subarrays in which the current element is min
                min_sum += (arr[mid] * left * right)
            
            mono_stack.append(i)

        return min_sum % (10 ** 9 + 7)
