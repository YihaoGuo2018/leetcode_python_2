class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]