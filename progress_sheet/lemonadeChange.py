class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        changes = defaultdict(int)

        for bill in bills:
            
            changes[bill] += 1

            change = bill - 5
            
            if change == 0:
                continue

            elif change == 15:
                
                # check if we can give one 10 and one 5
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                
                elif changes[5] > 2:
                    changes[5] -= 3
                
                else:
                    return False

            elif changes[change] > 0:
                changes[change] -= 1

            else:
                return False
        
        return True
