# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    dic = {}
    def verticalOrder(self, root):
        self.help(root, 1)
        save = []
        keys = sorted(self.dic.keys())
        for k in keys:
            save.append(self.dic[k])
        return save

    def help(self, root, depth):
        if root == None:
            return
        if depth not in self.dic.keys():
            self.dic[depth] = []
        self.dic[depth].append(root.val)
        self.help(root.left, depth - 1)
        self.help(root.right, depth + 1)
        return
