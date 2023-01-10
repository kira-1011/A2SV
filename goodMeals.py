class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        count_map = defaultdict(int)
        pairs = 0

        # Count occuerence
        for value in deliciousness:
            count_map[value] += 1
        
        # Look for pairs that sum up to a power of two
        for value1 in deliciousness:


            count_map[value1] -= 1

            for exp in range(22):

                value2 = (2 ** exp) - value1
                count = count_map[value2]

                if count != 0:
                    pairs += count

        return  pairs % (10**9 + 7)