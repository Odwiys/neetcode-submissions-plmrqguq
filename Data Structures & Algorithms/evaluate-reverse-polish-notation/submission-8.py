class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init stack (for numbers)
        # init array of expressions
        # iterate through stack
            # if it's an expression, take numbers from stack
            # else, append to stack
        # return stack[-1]

        # O(n)
        # O(n)

        stack = []
        expressions = ["+", "-", "/", "*"]

        for token in tokens:
            if token in expressions:
                b, a = stack.pop(), stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    stack.append(int(a / b))
                else:
                    stack.append(a * b)
            else:
                stack.append(int(token))

        return stack[-1]