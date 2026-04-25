class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res




        # total = 1
        # zeroes = 0
        # for num in nums:
        #     if num:
        #         total *= num
        #     else:
        #         zeroes += 1
        # if zeroes > 1: 
        #     return [0] * len(nums)

        # res = [0] * len(nums)
        # for i, c in enumerate(nums):
        #     if zeroes:
        #         res[i] = 0 if c else total
        #     else:
        #         res[i] = total // c

        # return res