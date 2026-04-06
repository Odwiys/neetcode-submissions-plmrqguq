class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if anagram
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT



        # # edge case if len not equal
        # if len(s) != len(t):
        #     return False

        # # init dicts to count
        # countS, countT = {} , {}


        # # iterate through
        # for i in range(len(s)):
        #     # get the countS based on the index of s and + 1. Do the same for countT
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # # return True/ False if they are the same
        # return countS == countT