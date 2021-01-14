class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic.keys():
                return n
            dic[n] = 0
