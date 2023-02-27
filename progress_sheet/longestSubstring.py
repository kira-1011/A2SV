class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        size = len(s)
        visited = set()
        longest = 0

        for right in range(size):

            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest
