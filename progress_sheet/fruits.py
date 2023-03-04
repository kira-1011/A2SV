class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        size = len(fruits)
        collected = defaultdict(int)
        max_fruits = 0

        # find the maximum fruits that can be collected
        for right in range(size):
                        
            collected[fruits[right]] += 1

            # we can only collect two types of fruits
            while len(collected) > 2:
                collected[fruits[left]] -= 1

                if collected[fruits[left]] == 0:
                    del collected[fruits[left]]

                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
