class Solution(object):
    def maxProfit(self, prices):
        global_profit = [[0 for _ in range(len(prices) + 1)] for _ in range(3)]

        save = []
        tmp = 0
        for price in prices:
            tmp += price
            save.append(price)
        for i in range(1, 3):
            local_profit = [0 for _ in range(len(prices))]
            for j in range(1, len(prices)):
                profit = save[j] - save[j - 1]
                tmp1 = global_profit[i - 1][j - 1] + profit
                tmp2 = global_profit[i - 1][j - 1]
                tmp3 = local_profit[j - 1] + profit
                local_profit[j] = max(tmp1, tmp2, tmp3)

                global_profit[i][j] = max(local_profit[j], global_profit[i][j - 1])
            print(local_profit)
        print(global_profit)
        out = 0
        for x in global_profit:
            out = max(max(x), out)
        return out

        """
        :type prices: List[int]
        :rtype: int
        """
