class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0
        seen = {}
        for x, num in enumerate(nums):
            print(f"x = {x}, num = {num}")
            complement = target - num
            if complement in seen:
                j = x
                i = seen[complement]
            else:
                seen[num] = x
        return [i, j]