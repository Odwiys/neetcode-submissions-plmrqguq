class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res
    #     res = ""
    #     for s in strs:
    #         res += str(len(s)) + "#" + s
    #     return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j



    #     res = []
    #     i = 0

    #     while i < len(s):
    #         j = i
    #         while s[j] != "#":
    #             j += 1
    #         length = int(s[i:j])
    #         i = j + 1
    #         j = i + length
    #         res.append(s[i:j])
    #         i = j

        return res

        # while i < len(s)
            # set j = i
            # increment j until we get #
            # get len of the s based on i:j
            # move i pointer to start of actual string
            # move j pointer to end of actual string
            # append decoded string to res
            # reset i = j