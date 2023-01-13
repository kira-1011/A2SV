class Solution:
    def printVertically(self, s: str) -> List[str]:

        vertcial_words = []
        max_size = 0
        s = s.split()

        # Find the maximum size
        for word in s:
            max_size = max(max_size, len(word))
        
        # Append each letter by vertically scanning s
        for index in range(max_size):

            vertical = []

            for word in s:

                size = len(word)

                if index < size:
                    vertical.append(word[index])
                
                else:
                    vertical.append(" ")

            vertical = "".join(vertical)

            # Remove trailing spaces
            vertical = vertical.rstrip()
            
            vertcial_words.append(vertical)
        
        return vertcial_words