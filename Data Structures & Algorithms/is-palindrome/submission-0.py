class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        array = list(s.replace(' ',''))
        cleaned = [s.lower() for s in array if s.isalnum()]
        reversed_array = cleaned[::-1]

        if cleaned == reversed_array:
            return True
        return False