class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        m = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1
                    dp[i] = max(dp[i], tmp)
                    m = max(m, dp[i])
        return m

        """
        :type nums: List[int]
        :rtype: int
        """
