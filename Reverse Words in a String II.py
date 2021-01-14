class Solution:
    def reverseWords(self, str: List[str]) -> None:
        save1 = "".join(str)
        save2 = save1.split(' ')
        save2 = save2[::-1]
        save3 = "".join(save2)
        for s in range(0,len(save3)):
            str[s] = save3[s]
        """
        Do not return anything, modify str in-place instead.
        """
