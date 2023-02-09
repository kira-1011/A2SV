class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        chemistry = 0
        left = 0
        right = len(skill) - 1

        # sort skill
        skill.sort()

        total = skill[left] + skill[right]

        # find the chemistry of each team
        while left < right:

            if total != (skill[left] + skill[right]):
                return -1
            
            chemistry += (skill[left] * skill[right])
            total = skill[left] + skill[right]

            left += 1
            right -= 1
        
        return chemistry
