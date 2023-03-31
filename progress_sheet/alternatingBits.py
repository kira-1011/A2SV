class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        shifted = n << 1
        bit_len = floor(log2(shifted) + 1)

        # if the number is even shift bits to the right
        if n % 2 == 0:
            shifted = n >> 1
            bit_len = floor(log2(n) + 1)

        alt_bits = n ^ shifted
        return alt_bits == (2 ** bit_len) - 1
