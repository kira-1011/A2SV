class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_count = Counter(p)
        s_count = defaultdict(int)
        s_len = len(s)
        p_len = len(p)
        indices = []

        if p_len > s_len:
            return []

        # Construct window
        for i in range(p_len):
            s_count[s[i]] += 1
        
        if s_count == p_count:
            indices.append(0)
        
        for right in range(p_len, s_len):

            s_count[s[right - p_len]] -= 1
            s_count[s[right]] += 1

            if s_count[s[right - p_len]] == 0:
                del s_count[s[right - p_len]]
            
            if s_count == p_count:
                indices.append(right - p_len + 1)
        
        return indices
