class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        letter_count = Counter(words[0])
        answer = []

        for word in words[1 : ]:

            curr_count = Counter(word)

            for letter in letter_count:

                if letter in curr_count:
                    letter_count[letter] = min(letter_count[letter], curr_count[letter])
                
                else:
                    letter_count[letter] = 0
        
        for letter in letter_count:
            answer.extend(letter * letter_count[letter])
        
        return answer
