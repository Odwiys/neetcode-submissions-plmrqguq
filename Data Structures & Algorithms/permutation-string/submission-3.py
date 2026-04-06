class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        for r in range(len(s2)):
            sliceds2 = s2[l:r + len(s1)]
            print(sliceds2)
            if sorted(sliceds2) == sorted(s1):
                return True
            l += 1

        return False