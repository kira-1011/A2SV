class Solution:
    def findComplement(self, num: int) -> int:

        stop_bit = floor(log2(num) + 1)
        mask_bit = 2 ** stop_bit - 1

        num ^= mask_bit
        return num
