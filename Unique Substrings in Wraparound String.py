class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        values = collections.defaultdict(int)
        last_c, last_v = "", 0
        for c in p:
            v = last_v + 1 if last_c and (ord(c) - ord(last_c)) % 26 == 1 else 1
            values[c] = max(values[c], v)
            last_c, last_v = c, v
        return sum(values.values())