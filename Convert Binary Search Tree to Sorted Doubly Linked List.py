"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return root
        savehead = Node(0)

        if root:
            self.help(root, savehead)
        tmp = savehead
        while tmp.left:
            tmp = tmp.left

        ##print(tmp.val)

        out = Node(0)
        out.right = tmp
        tmp.left = savehead.left
        savehead.left.right = tmp

        ##print(tmp.left.right.val)
        return out.right

    def help(self, curr, insertplace):

        left = curr.left
        right = curr.right

        curr.right = insertplace
        insertplace.left = curr

        if left:
            self.help(left, curr)

        if right:
            self.help(right, insertplace)
            right.left = curr
            curr.right = right
        return 

