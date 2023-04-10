n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
nums.append(0)

if k == 0:
    
    if nums[k] == 1:
        print(-1)
    
    else:
        print(nums[k] - 1)

elif nums[k] == nums[k - 1]:
    print(-1)

else:
    print(nums[k - 1])
