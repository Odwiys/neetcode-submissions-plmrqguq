class Solution:
    def trap(self, height: List[int]) -> int:
        # check if not height, return 0
        # init l, r pointers
        # init leftMax and rightMax
        # init res

        # while l < r
            # check if leftMax < rightMax
                # increment left pointer
                # set new leftMax
                # add res if can trap water (leftMax - height at l)
            # else
                # decrement right pointer
                # set new rightMax
                # add res if can trap water (rightMax - height at r)
        # return res

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


