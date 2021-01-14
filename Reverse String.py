class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[0:] = s[::-1]

        """
        Do not return anything, modify s in-place instead.
        """
