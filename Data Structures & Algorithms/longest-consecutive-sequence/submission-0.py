class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # init longest
        # change nums to set
        # iterate through set
            # check if start of sequence (if n-1 in set)
                # set length to 0
                # if start of sequence 
                    # while n in set - in this case need to add length
                    # increase length + 1
                # compare longest

        # return longest

        longest = 0
        numsSet = set(nums)
        for num in numsSet:
            if (num-1) not in numsSet:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest
