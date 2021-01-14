class Solution(object):
    def __init__(self):
        self.target = 0

    def help_sort(self, a):
        return abs(a - self.target)

    def findClosestElements(self, arr, k, x):
        self.target = x
        arr.sort(key=self.help_sort)
        tmp = arr[0: k]
        tmp.sort()
        return tmp
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
