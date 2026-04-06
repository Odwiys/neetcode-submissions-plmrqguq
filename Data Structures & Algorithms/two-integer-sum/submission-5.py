class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init 2 pointers
        # store seen numbers & their indexes

        # iterate through nums
        # find the complement (it would be a number in seen)
        # if found, 1st pointer will be seen number, 2nd will be current index

        i,  j = 0, 0
        seen = {}

        for x, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                j = x
                i = seen[complement]
            else:
                seen[num] = x

        return [i, j]


        