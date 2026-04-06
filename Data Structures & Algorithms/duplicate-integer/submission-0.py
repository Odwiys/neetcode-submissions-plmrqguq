class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        routed_array = []
        for num in nums:
            if num not in routed_array:
                routed_array.append(num)
            else:
                return True

        return False
        