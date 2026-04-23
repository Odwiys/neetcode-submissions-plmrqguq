class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i, j = 0, 0

        for x, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                i = seen[compliment]
                j = x 
                return [i , j]
            
            seen[num] = x

        return [i, j]