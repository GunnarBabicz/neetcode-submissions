class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        # sliding window
        while r < len(prices):
            if prices[l] < prices[r]: #left and right are one apart beginning. If right is lower than left, then it will be the newest discovered lowest value
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r
            r += 1
        return max_profit
