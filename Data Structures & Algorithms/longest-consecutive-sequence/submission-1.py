class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # define longest
        longest = 0
        # set nums as a hashset
        numsSet = set(nums)
        # iterate through nums
        for num in nums:
            # init length
            length = 0
            # if left neighbor of nums not in set (it is the start of squence)
            if (num - 1) not in numsSet:
                # increment length until not in set
                while (num + length) in numsSet:
                    length += 1
                # check which is longer
                longest = max(length, longest)

        return longest