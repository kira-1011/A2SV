class Solution:

    # Compute arthimetic operations based on the given operator
    def compute(self, operand1, operand2, operator):

        if operator == '+':
            return operand1 + operand2

        if operator == '-':
            return operand1 - operand2
        
        if operator == '/':
            return int(operand1 / operand2)

        if operator == '*':
            return operand1 * operand2
        
        return 0

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                res = self.compute(int(operand1), int(operand2), token)
                stack.append(res)

        return stack[0]
