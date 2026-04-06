class Solution:

    def encode(self, strs: List[str]) -> str:
        # create single string (length + delimiter + string)
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # init result n i 
        res, i = [] , 0
        # while i < len of str
        while i < len(s):
            # set j as i (using second pointer to find end of string)
            j = i
            # while j is not "delimiter"
            while s[j] != "#":
                # increment j (this finds the end of the integer/ length)
                j += 1
            # set length of string into integer
            length = int(s[i:j])
            # append string to res based on j
            res.append(s[j + 1: j + 1 + length])
            # increment i
            i = j + 1 + length
        return res
