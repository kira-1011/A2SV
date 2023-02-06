class Solution:
    
    def flip(self, arr, end):

        half = end // 2

        # flip the array
        for i in range(half):
            arr[i], arr[end - 1 - i] = arr[end - 1 - i], arr[i]

    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []
        size = len(arr)

        # find the maximum from the subarray and flip the array
        for curr_size in range(size - 1, -1, -1):

            max_idx = 0
            for i in range(curr_size + 1):
                if arr[max_idx] < arr[i]:
                    max_idx = i
                
            self.flip(arr, max_idx + 1)
            print(arr)
            self.flip(arr, curr_size + 1)
            print(arr)

            flips.append(max_idx + 1)
            flips.append(curr_size + 1)
        
        return flips
