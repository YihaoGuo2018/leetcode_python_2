class Solution(object):
    def maxProfit(self, prices):
        out = 0
        i = 0
        while i < len(prices):
            print(i)
            profit = 0
            pre = prices[i]
            j = i
            j += 1
            while j < len(prices) and prices[j] > pre:
                profit += prices[j] - pre
                pre = prices[j]
                j += 1
            out += profit
            i = j
        return out
        """
        :type prices: List[int]
        :rtype: int
        """
