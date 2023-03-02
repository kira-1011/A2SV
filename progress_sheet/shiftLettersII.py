class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        # Line sweeping technique
        s_len = len(s)
        prefix_shifts = [0] * (s_len + 1)
        shifted = []

        # Mark the starting point and ending point for each shifts
        # mark 1 if it's forward shift for starting point and -1 for ending point
        # mark -1 if it's backward shift for starting point and 1 for ending point
        for shift in shifts:
            direction = 1

            # if shift direction is backward decrease by 1
            if shift[2] == 0:
                direction = -1

            prefix_shifts[shift[0]] += direction
            prefix_shifts[shift[1] + 1] -= direction

        # Sweep the marked points by taking the cumulative sum 
        # to find the total shifts for each letter
        for i in range(1, s_len):
            prefix_shifts[i] += prefix_shifts[i - 1]

        # Shift each letter
        for i in range(s_len):
            
            # Wrap around the shift
            increment = (ord(s[i]) - ord('a') + prefix_shifts[i]) % 26
            shifted.append(chr(ord('a') + increment))
    
        return "".join(shifted)
