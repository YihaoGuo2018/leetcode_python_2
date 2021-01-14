class Solution(object):
    def isInterleave(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [[True for _ in xrange(c + 1)] for _ in xrange(r + 1)]
        for i in xrange(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        print(dp)
        for i in xrange(1, r + 1):
            for j in xrange(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]