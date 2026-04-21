class Solution:
    def isValid(self, s: str) -> bool:
        method = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:
            if c in method:
                if stack and stack[-1] != method[c]:
                    return False
                elif stack:
                    print("here?")
                    stack.pop()
                else:
                    return False
                print("here 1?")
            else:
                stack.append(c)

        print(stack)

        return True if not stack else False
