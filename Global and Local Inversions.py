class Solution(object):
    def isIdealPermutation(self, A):
            cmax = 0
            for i in range(len(A) - 2):
                cmax = max(cmax, A[i])
                if cmax > A[i + 2]:
                    return False
            return True