class Solution(object):
    def maxRotateFunction(self, A):
        r = curr = sum(i * j for i,j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r