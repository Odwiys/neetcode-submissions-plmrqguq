class Solution:
    # import re
    # def isPalindrome(self, s: str) -> bool:
    #     array = list(s.replace(' ',''))
    #     cleaned = [s.lower() for s in array if s.isalnum()]
    #     reversed_array = cleaned[::-1]

    #     if cleaned == reversed_array:
    #         return True
    #     return False

    def isPalindrome(self, s:str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True
