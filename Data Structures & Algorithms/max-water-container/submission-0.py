class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init res
        # init 2 pointers
        # while l < r:
            # calculate area (length * height(min))
            # compare which area is larger w res
            # move pointer of the lower height

        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        