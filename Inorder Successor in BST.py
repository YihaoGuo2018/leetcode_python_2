# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    l = []
    def inorderSuccessor(self, root, p):
        self.help(root)
        if p not in self.l:
            return False
        if self.l.index(p) == len(self.l) - 1:
            return False
        return self.l[self.l.index(p) + 1]
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
    def help(self, node):
        if node == None:
            return
        self.help(node.left)
        self.l.append(node.val)
        self.help(node.right)
