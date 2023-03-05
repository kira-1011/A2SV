class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        score = 0

        # calculate intermediate score and push it to the stack
        for paranth in s:

            if paranth == '(':
                stack.append(paranth)
            
            elif stack[-1] == "(":
                stack.pop()
                stack.append(1)
            
            else:
                temp_score = 0
                while stack[-1] != "(":
                    temp_score += stack.pop()
                
                stack.pop()
                stack.append(temp_score * 2)

        # get the total score
        while stack:
            score += stack.pop()

        return score
