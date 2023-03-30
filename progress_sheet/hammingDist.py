class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        # Mark the bits which are different using XOR
        pos_bits = x ^ y
        distance = 0

        # handle if there is no difference
        if pos_bits == 0:
            return distance

        # calculate the bit length
        bit_len = floor(log2(pos_bits) + 1)

        # count the 1's which mark the difference
        for k in range(bit_len):
            test_bit = (pos_bits & (1 << k)) != 0
            distance += (test_bit)
        
        return distance
