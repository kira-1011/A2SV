test_cases = int(input())

for _ in range(test_cases):
    
    size = int(input())
    remaining = size
    nums = list(map(int, input().split()))
    
    nums.sort()
    for i in range(1, size):
        
        diff = abs(nums[i - 1] - nums[i])
        
        if diff == 1 or diff == 0:
            remaining -= 1
        
    if remaining == 1:
        print("YES")
    else:
        print("NO")
