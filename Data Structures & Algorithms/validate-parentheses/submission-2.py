class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        method = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in s:
            if char in method:
                # Check if it links to last item in stack
                if stack and stack[-1] == method[char]:
                    stack.pop()
                else:
                    return False
            else:
                # add it to the stack
                stack.append(char)

        return True if not stack else False











        # stack = []
        # method = {"]": "[", "}":"{", ")": "("}

        # for c in s:
        #     if c in method:
        #         if stack and stack[-1] == method[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return True if not stack else False