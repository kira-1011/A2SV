maxAvg = -float('inf')
size = len(nums)
current = 0
left = 0

# construct window
for i in range(k):
    current += nums[i]

maxAvg = max(maxAvg, current)

for right in range(k, size):
    current -= nums[left]
    current += nums[right]
    maxAvg = max(maxAvg, current)
    left += 1

return maxAvg / k
