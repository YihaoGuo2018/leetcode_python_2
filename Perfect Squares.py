class Solution(object):
    def numSquares(self, n):
        begin = n // 2
        while begin * begin > n:
            begin -= 1

        save = []
        while begin > 0:
            save.append(begin * begin)
            begin -= 1

        dp = [i for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for num in save:
                if num <= i:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[n]

        """
        :type n: int
        :rtype: int
        """
