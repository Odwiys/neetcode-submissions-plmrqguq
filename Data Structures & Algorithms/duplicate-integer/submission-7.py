class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False



















        # seen = []
        # for num in nums:
        #     if num not in seen:
        #         seen.append(num)
        #     else:
        #         return True
        
        # return False










        # routed_array = []
        # for num in nums:
        #     if num not in routed_array:
        #         routed_array.append(num)
        #     else:
        #         return True

        # return False
        