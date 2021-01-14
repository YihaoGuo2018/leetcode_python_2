class Solution(object):
    def maxProfit(self, prices):
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        # 0: mai
        # 1: meimai
        for i in range(1, len(prices) + 1):
            for j in range(1, i):
                profit = prices[i - 1] - prices[j - 1]
                tmp = 0
                if j - 2 >= 0:
                    tmp = dp[j - 2][0]
                if j - 1 >= 0:
                    tmp = max(tmp, dp[j - 1][1])

                dp[i][0] = max(dp[i][0], tmp + profit)
            tmp = 0
            if i - 2 >= 0:
                tmp = max(dp[i - 2][1], dp[i - 2][0])
            if i - 1 >= 0:
                tmp = max(dp[i - 1][1], dp[i - 1][0])

            dp[i][1] = tmp

        print(dp)
        return max(dp[-1])


