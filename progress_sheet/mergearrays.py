# Receive inputs
size1, size2 = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

left = 0
right = 0
merged_arr = []

arr1.append(float('inf'))
arr2.append(float('inf'))

for i in range(size1 + size2):
    
    if arr1[left] <= arr2[right]:
        merged_arr.append(arr1[left])
        left += 1
    
    else:
        merged_arr.append(arr2[right])
        right += 1
        
print(*merged_arr)
