class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # A ceiling is max sum allowed for earch segment (subarray).
        def isValidCeiling(nums, m, ceiling):
            count, total = 1, 0  # count - # of segments. total - temp sum of the current segment.
            for i in range(len(nums)):
                if total + nums[i] <= ceiling:
                    total += nums[i]  # add the number to the current segment.
                else:
                    total = nums[i]    # over the ceiling, start a new segment.
                    count += 1
                if (count > m):
                    return False # if need more segments than m, the this an invalid ceiling.
            return True # if count <= m, then this is a valid ceiling, i.e. if we can split into less than M segments, sure enough we can split into M segments.

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if isValidCeiling(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l