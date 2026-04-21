class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for x, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                i = seen[compliment]
                j = x
                return [i, j]
            else:
                # add num and index
                seen[num] = x
