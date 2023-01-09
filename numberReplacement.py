from collections import defaultdict

def replaceNumbers(nums, letters):

    # Intialize all needed variables
    index_map = defaultdict(list)
    # replaced = [""] * arr_len

    # store the value as key and list of its occurence indices as value
    for index, num in enumerate(nums):
        index_map[num].append(index)
    
    # replace 
    for index, letter in enumerate(letters):
        number = nums[index]
        indices = index_map[number]

        for num_index in indices:
            nums[num_index] = letter
    
    nums = "".join(nums)
    return nums

# Accept number of test cases
test_cases = int(input())

# Accept all inputs
for i in range(test_cases):
    
    arr_len = int(input())
    nums = input().split()
    nums = list(map(int, nums))
    letters = input()

    replaced = replaceNumbers(nums, letters)

    if replaced == letters:
        print("YES")

    else:
        print("NO")