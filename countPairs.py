class Solution:
    
    def removeDuplicate(self, word):

        # Remove duplicates
        word = set(word)
        word = "".join(word)

        return word
    
    def sortWord(self,word):

        # Sort the given word
        word = sorted(word)
        word = "".join(word)

        return word
    
    def countPairs(self, words):

        # Count pairs
        word_count = defaultdict(int)
        pairs = 0

        for word in words:
            word_count[word] += 1
        
        for count in word_count.values():
            pairs += ((count * (count - 1)) // 2)
        
        return pairs

    def similarPairs(self, words: List[str]) -> int:

        # Remove duplicates in the given words
        for index, word in enumerate(words):
            words[index] = self.removeDuplicate(word)
        
        # Sort the words in the list
        for index, word in enumerate(words):
            words[index] = self.sortWord(word)
        
        #  Count Pairs Of Similar Strings
        pairs = self.countPairs(words)

        return pairs

