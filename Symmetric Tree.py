# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        out = self.help(root.left, root.right)
        return out
    def help(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        if left.val != right.val:
            return False
        ok1 = self.help(left.right, right.left)
        ok2 = self.help(right.right, left.left)
        if ok1 == False or ok2 == False:
            return False
        return True
