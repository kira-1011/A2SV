class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        len2 = len(s2)
        s1_count = Counter(s1)

        if len1 > len2:
            return False

        # Construct window
        for i in range(len1):
            if s2[i] in s1_count:
                 s1_count[s2[i]] -= 1
        
        # compare the letter count of s2 window with s1
        for right in range(len1, len2):
            
            # Check if all values are 0 in dictionary
            if not any(s1_count.values()):
                return True

            if s2[right] in s1_count:
                s1_count[s2[right]] -= 1
            
            if s2[right - len1] in s1_count:
                s1_count[s2[right - len1]] += 1
            
        # Check if all values are 0 in dictionary
        if not any(s1_count.values()):
            return True

        return False
