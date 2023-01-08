class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_index = {}

        # Store each character's index
        for index, char in enumerate(order):
            order_index[char] = index

        words_len = len(words)     

        # compare adjacent strings based on the given order
        for word_idx in range(1, words_len):
            
            word = words[word_idx]
            prev_word = words[word_idx - 1]
            word_len = len(word)
            prev_word_len = len(prev_word)
            max_len = max(len(word), len(prev_word))

            for i in range(max_len):

                if i < word_len and i < prev_word_len:

                    if order_index[word[i]] < order_index[prev_word[i]]:
                        return False
                
                    if order_index[word[i]] > order_index[prev_word[i]]:
                        break
                    
                    print(prev_word, word)
                                
                elif prev_word_len > word_len:
                        return False
                                    
        return True