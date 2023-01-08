class Solution:
    def freqAlphabets(self, s: str) -> str:

        # Intialize all needed varibales
        size = len(s)
        index = size - 1
        mapped_string = []
        integer = 0

        # Map integers to alphabets
        while index >= 0:

            if s[index] == "#":
                integer = int(s[index - 2 : index])
                index -= 3

            else:
                integer = int(s[index])
                index -= 1
            
            alphabet = ord('a') + integer - 1 
            mapped_string.append(chr(alphabet))

        # Reverse the final answer
        mapped_string.reverse()
        mapped_string = "".join(mapped_string)
        

        return mapped_string