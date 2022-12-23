class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize left and right pointer
        n = len(word1)
        m = len(word2)
        left = 0
        right = 0
        temp = ""
        merged_string = []

        min_len = min(n, m)

        # Append to merged_string alternative characters between word1 and word2
        while left < min_len:
            temp = word1[left] + word2[right]
            merged_string.append(temp)
            left += 1
            right += 1
        
        # Append the remaining characters
        merged_string.append(word1[left:])
        merged_string.append(word2[right:])

        # Join into one single string
        merged_string = "".join(merged_string)
            
        return merged_string