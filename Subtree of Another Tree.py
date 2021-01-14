# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def isMatch(self, s, t):
#         if not (s and t):
#             return s is t
#         return (s.val == t.val and
#                 self.isMatch(s.left, t.left) and
#                 self.isMatch(s.right, t.right))

#     def isSubtree(self, s, t):
#         if self.isMatch(s, t): return True
#         if not s: return False
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def convert(p):
            return "，" + str(p.val) + convert(p.left) + convert(p.right) if p else "$"

        print(convert(t))
        return convert(t) in convert(s)
