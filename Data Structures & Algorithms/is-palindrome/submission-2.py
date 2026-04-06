class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init 2 pointers
        # iterate through two pointers to check if same
            # if non alphanumeric we skip

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True
        