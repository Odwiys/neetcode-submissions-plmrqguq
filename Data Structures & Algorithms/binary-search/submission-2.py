class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init 2 pointers
        # while i >= 0 and i <= len(nums)
            # get mid index
            # is nums[i] = target if no?
                # if lesser, half the i from start
                # if greater, half the i from end
            # else return index
        # return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1 