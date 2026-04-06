class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        if t == "":
            return ""
        
        if len(t) > len(s):
            return ""

        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need, res, resLen = 0, len(countT), [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # update our result if lesser than resLen
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # pop from the left of window
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""