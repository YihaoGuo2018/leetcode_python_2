# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k) :
        s = set()
        def dfs(node):
            if node == None:
                return False
            if k - node.val in s:
                return True
            s.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
s = set()
s.add(1)
s.add(2)
print(s)