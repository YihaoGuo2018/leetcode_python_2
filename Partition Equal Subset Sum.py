class Solution(object):
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target]
        if target == 0:
            d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in xrange(ind, n):
                    if self.canFindSum(nums, target - nums[i], i + 1, n, d):
                        d[target] = True
                        break
        return d[target]

    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s / 2, 0, len(nums), {})