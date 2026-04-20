class Solution:
    def isValid(self, s: str) -> bool:
        method = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for char in s:
            if char in method:
                if stack and method[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False















        # method = {
        #     ")" : "(",
        #     "}" : "{",
        #     "]" : "["
        # }
        # stack = []

        # for char in s:
        #     if char in method:
        #         if stack and method[char] == stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)

        # return True if not stack else False

