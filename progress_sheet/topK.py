class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        nums_freq = list(zip(freq.keys(), freq.values()))
        size = len(nums_freq)
        top_k = []

        # handle edge case
        if size == 1:
            return [nums[0]]

        # select the top k frequent elements
        pivot, left, right = -1, 0, size - 1

        while pivot != size - k:

            pivot = left
            write = left + 1

            for read in range(left + 1, right + 1):

                if nums_freq[read][1] <= nums_freq[pivot][1]:
                    nums_freq[read], nums_freq[write] = nums_freq[write], nums_freq[read]
                    write += 1
            
            nums_freq[pivot], nums_freq[write - 1] = nums_freq[write - 1], nums_freq[pivot]
            pivot = write - 1

            if pivot < size - k:
                left = pivot + 1

            else:
                for i in range(right, pivot - 1, -1):
                    top_k.append(nums_freq[i][0])
                right = pivot - 1
        
        return top_k
