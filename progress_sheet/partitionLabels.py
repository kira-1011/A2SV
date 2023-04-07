class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        recent_idx = defaultdict(int)
        size = len(s)
        left = -1
        right = 0
        partitions = []

        for i in range(size):
            recent_idx[s[i]] = i
        
        right = recent_idx[s[right]]

        for i in range(size):

            if i == right:
                partitions.append(right - left)
                left = i

                if i + 1 < size:
                    right = recent_idx[s[i + 1]]

            elif recent_idx[s[i]] > right:
                right = recent_idx[s[i]]

        return partitions
