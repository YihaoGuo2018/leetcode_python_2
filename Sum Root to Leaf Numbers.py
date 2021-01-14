# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    sum = 0
    def sumNumbers(self, root):
        out = help(root)
        return self.sum
        """
        :type root: TreeNode
        :rtype: int
        """
    def help(self, root, old):
        if root == None:
            self.sum += old
        new = old * 10 + root.val
        self.help(root.left, new)
        self.help(root.right, new)