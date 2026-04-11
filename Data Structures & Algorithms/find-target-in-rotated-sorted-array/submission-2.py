class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # identify left or right side of array from mid is sorted
            if nums[m] >= nums[l]: # left side is sorted
                # if target > nums[m] or target < nums[l]: # target not on left side, go right
                #     l = m + 1
                # else: # target is on the left side, go left
                #     r = m - 1

                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else: # right side is sorted
                # if target < nums[m] or target > nums[r]: # target is on left, go left
                #     r = m - 1
                # else:
                #     l = m + 1

                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
