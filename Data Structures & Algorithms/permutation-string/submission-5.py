class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # convert s1 into a dict
        # sliding window conversion of s2 as a dict
        # compare with s1
        if len(s1) > len(s2):
            return False

        s1freq = {}
        for char in s1:
            s1freq[char] = 1 + s1freq.get(char, 0)

        l = 0
        for r in range(len(s2)):
            s2slice = s2[l:r + len(s1)]
            s2freq = {}
            for char in s2slice:
                s2freq[char] = 1 + s2freq.get(char, 0)
            l += 1
            if s1freq == s2freq:
                return True

            
        return False