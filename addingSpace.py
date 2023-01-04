class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        # Intialize modified string
        modified_string = []
        space_size = len(spaces)
        string_size = len(s)
        right = 0

        # Insert spaces at the indices
        for left in range(string_size):

            if right < space_size and left == spaces[right]:
                modified_string.append(" ")
                right += 1
            
            modified_string.append(s[left])

        # Join the last modified string
        modified_string = "".join(modified_string)

        return modified_string