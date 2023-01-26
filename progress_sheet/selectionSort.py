class Solution: 
    def select(self, arr, i):
        
        min_index = i

        for j in range(i + 1, n):
            
            if arr[min_index] > arr[j]:
                min_index = j
        
        return min_index
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            
            min_index = self.select(arr, i)
            
            arr[min_index], arr[i] = arr[i], arr[min_index]