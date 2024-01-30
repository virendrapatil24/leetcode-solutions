class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == '+':
                    res = operand1 + operand2   
                elif token == '-':
                    res = operand1 - operand2  
                elif token == '*':
                    res = operand1 * operand2  
                elif token == '/':
                    res = int(operand1 / operand2)
                stack.append(str(res))  
            else:
                stack.append(token)
        return int(stack[-1])  