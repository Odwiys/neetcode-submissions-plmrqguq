class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init res [] * len(nums)
        # iterate through nums:
            # if num is at pointer, skip, else multiply
            # append to res
        # return res

        res = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]

            res[i] = prod
        return res

