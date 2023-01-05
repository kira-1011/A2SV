class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix_string = []
        min_word_len = len(strs[0])
        is_common_prefix = True

        # Find the minimum word length
        for word in strs:
            min_word_len = min(min_word_len, len(word))
        
        # Vertically scan all strings to find common prefix
        for i in range(min_word_len):

            common_prefix = strs[0][i]

            for prefix in strs:
                
                if prefix[i] != common_prefix:
                    common_prefix = ""
                    is_common_prefix = False
                    break
                
                common_prefix = prefix[i]
            
            if not is_common_prefix:
                break
            
            prefix_string.append(common_prefix)

        return "".join(prefix_string)