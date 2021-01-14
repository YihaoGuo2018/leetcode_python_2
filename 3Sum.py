class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = set([])
        for i in range(len(nums) - 2):
            num1 = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                mysum = num1 + nums[l] + nums[r]
                if mysum == 0:
                    res = (num1, nums[l], nums[r])
                    result.add(res)
                    l += 1
                    r -= 1

                elif mysum > 0:
                    r -= 1
                else:
                    l += 1

        return list(result)