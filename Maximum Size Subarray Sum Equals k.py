class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dic = {0: -1}
        sum +=0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in dic.keys():
                continue
            dic[sum] = i
        max_i = 0
        for t in dic.keys():
            if t - k in dic.keys():
                max_i = max(max_i,dic[t] - dic[t-k])
