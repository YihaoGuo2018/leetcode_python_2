# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        if root == None:
            return None, None
        val1, dif1 = self.closestValue(root.left, target)
        val2, dif2 = self.closestValue(root.right, target)
        val3, dif3 = root.val, abs(root.val - target)
        if val1 != None:
            if dif1 < dif3:
                val3 = val1
                dif3 = dif1
        if val2 != None:
            if dif2 < dif3:
                val3 = val2
                dif3 = dif2
        return val3, dif3