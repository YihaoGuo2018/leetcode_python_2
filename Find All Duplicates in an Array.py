class Solution(object):
    def findDuplicates(self, nums):
        tmpl = len(nums) + 1
        for i in range(len(nums)):
            values = nums[i] % tmpl

            nums[values - 1] += tmpl
        out = []

        for i in range(len(nums)):
            if nums[i] // tmpl == 2:
                out.append(i + 1)
        return out
        """
        :type nums: List[int]
        :rtype: List[int]
        """
