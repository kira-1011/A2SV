class Word:

    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    # override the less-than operator so that the element at the top of the min heap has the least frequency and
    # the lexicographically larger word
    def __lt__(self, next):

        if self.count == next.count:
            return self.word > next.word
        
        return self.count < next.count

class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)
        word_count = []
        top_k = []

        for word, count in freq.items():
            
            heappush(word_count, Word(count, word))

            if len(word_count) > k:
                heappop(word_count)

        while len(top_k) < k:
            top_k.append(heappop(word_count).word)

        top_k.reverse()

        return top_k 
