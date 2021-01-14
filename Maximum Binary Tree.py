# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        root = max(nums)
        index = nums.index(root)
        Trnode = TreeNode(root)
        Trnode.left = self.constructMaximumBinaryTree(nums[0:index])
        Trnode.right = self.constructMaximumBinaryTree(nums[index + 1:len(nums)])
        return Trnode
