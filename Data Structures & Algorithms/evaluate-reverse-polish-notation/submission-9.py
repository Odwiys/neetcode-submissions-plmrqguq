class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        maffs = ["+", "-", "*", "/"]

        for token in tokens:
            if token in maffs:
                first_digit = int(stack[-2])
                second_digit = int(stack[-1])
                if token == "+":
                    new_digit = first_digit + second_digit
                elif token == "-":
                    new_digit = first_digit - second_digit
                elif token == "*":
                    new_digit = first_digit * second_digit
                else:
                    new_digit = first_digit / second_digit
                stack.pop()
                stack.pop()
                stack.append(new_digit)
            else:
                stack.append(token)

        return int(stack[-1])