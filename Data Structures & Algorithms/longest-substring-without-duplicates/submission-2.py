class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init set
        # init l
        # init res

        # for r in range(len(s)):
            # while s[r] in charset:
                # remove l
                # increment l
            # add s[r] to set
            # get max res
        # return res

        charSet = set()
        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res












        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res