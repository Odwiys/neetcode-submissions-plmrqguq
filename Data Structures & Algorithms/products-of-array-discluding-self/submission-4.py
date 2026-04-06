class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init res [] * len(nums)
        # iterate through nums:
            # if num is at pointer, skip, else multiply
            # append to res
        # return res

        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

