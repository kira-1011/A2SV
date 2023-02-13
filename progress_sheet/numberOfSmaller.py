size1, size2 = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

# to handle last elements
nums1.append(float('inf'))

index1 = 0
index2 = 0
smallerCount = [0] * size2
smaller = 0

# count smaller numbers
while index1 < size1 + 1 and index2 < size2:
    
    if nums1[index1] < nums2[index2]:
        smaller += 1
        index1 += 1
    
    else:
        smallerCount[index2] += smaller
        index2 += 1

print(*smallerCount)
