class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create res based on len of nums
        # set prefix of 1
        # iterate through nums
            # set res to prefix
            # multiply prefix to nums
        # set postfix to 1
        # iterate through nums reversed
            # set res to multiply w postfix
            # multiply postfix to nums
        # return res

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res