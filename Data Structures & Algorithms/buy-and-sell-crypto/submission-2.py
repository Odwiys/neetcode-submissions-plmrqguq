class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers to find the min and max
        # init pointers (first and second/ 0, 1)
        # init maxProfit
        # while r < len(prices)
            # if prices[r] > prices[l]:
                # maxProfit = max(maxProfit, price[r] - price[l])
            # else:
                # l = r
            # r += 1
        # return maxProfit

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit