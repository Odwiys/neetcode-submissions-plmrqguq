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

        # res = [1] * len(nums)
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) -1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res

        # det product of all nums
        # iterate through and divide by itself

        output = [[1] for i in range(len(nums))]
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        
        if zero_count > 1: return [0] * len(nums)

        for i, c in enumerate(nums):
            if zero_count:
                if c: #checking if non-0
                    output[i] = 0
                else:
                    output[i] = product
            else:
                output[i] = product // c

        return output










