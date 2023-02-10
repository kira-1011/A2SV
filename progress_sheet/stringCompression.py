class Solution:
    
    # Overwrite the number of occurenece of a character
    def writeOccurence(self, chars, write, count):
        
        if count != 1:
            count = str(count)

            for char in count:
                chars[write] = char
                write += 1

        return write

    def compress(self, chars: List[str]) -> int:

        size = len(chars)
        left = 0
        write = 0

        # append empty character to handle the last element
        chars.append(" ")

        if size == 1:
            return 1

        # when a new character is found write the occurence and go to the next character
        for right in range(size + 1):
            
            if chars[left] != chars[right]:

                chars[write] = chars[left]
                count = right - left
                write += 1

                # write the occurence only when it is greater than 1
                write = self.writeOccurence(chars, write, count)
                    
                left = right
        
        return write
