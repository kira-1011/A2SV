def countingSort(arr):
    
    size = len(arr)
    count_arr = [0] * 100
    
    for num in arr:
        count_arr[num] += 1
    
    return count_arr