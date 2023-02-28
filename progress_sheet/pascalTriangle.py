class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        # Store the previous pascal triangle and track the current pascal triangle
        prev_pascal = self.getRow(rowIndex - 1)
        current_pascal = [1]

        # Sum up the two numbers directly above the current pascal triangle 
        for i in range(1, rowIndex):
            current_pascal.append(prev_pascal[i] + prev_pascal[i - 1])
        
        current_pascal.append(1)

        return current_pascal
