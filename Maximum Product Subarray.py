class Solution(object):
    def maxProduct(self, A):
            B = A[::-1]
            for i in range(1, len(A)):
                A[i] *= A[i - 1] or 1
                B[i] *= B[i - 1] or 1
            print(2 or 1)
            print(A)
            print(B)
            c = (A + B)
            print(c)
            return max(A + B)