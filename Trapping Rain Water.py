class Solution(object):
    def trap(self, height):
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i - 1])
            ans = ans + h1 + h2 - height[i]
        return ans - len(height) * h1