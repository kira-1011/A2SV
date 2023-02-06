class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        size = len(arr)
        greatest = -1
        arr.append(greatest)

        for i in range(size - 1, -1, -1):
            max_n = max(arr[i], greatest)
            arr[i] = greatest
            greatest = max_n

        arr.pop()
        
        return arr
