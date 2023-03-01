class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        len2 = len(s2)
        s1_count = Counter(s1)
        s2_count = defaultdict(int)

        if len1 > len2:
            return False

        # Construct window
        for i in range(len1):
            s2_count[s2[i]] += 1
        
        # compare the letter count of s2 window with s1
        for right in range(len1, len2):

            if s1_count == s2_count:
                return True
            
            s2_count[s2[right]] += 1
            s2_count[s2[right - len1]] -= 1

            if s2_count[s2[right - len1]] == 0:
                del s2_count[s2[right - len1]]
        
        if s1_count == s2_count:
            return True

        return False
