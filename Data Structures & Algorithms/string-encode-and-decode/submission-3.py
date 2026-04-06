class Solution:

    def encode(self, strs: List[str]) -> str:
        # create single string (length + delimiter + string)
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # init result n i 
        # while i < len of str
            # set j as i (using second pointer to find end of string)
            # while j is not "delimiter"
                # increment j (this finds the end of the integer/ length)
            # set length of string into integer
            # append string to res based on j
            # increment i
        # return res
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
        