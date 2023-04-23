class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        # z y x w v u t s r q p o n m l k j i h g f e d c b a

        max_product = 0
        words_count = []

        for i in range(len(words)):

            word1_count = 0

            for char in words[i]:

                # store letter occurence using bit
                mask = 1
                shift = ord(char) - ord('a')

                word1_count |= (mask << shift)
                
            words_count.append(word1_count)
        
        for i in range(len(words) - 1):

            for j in range(i + 1, len(words)):

                if (words_count[i] & words_count[j]) == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
