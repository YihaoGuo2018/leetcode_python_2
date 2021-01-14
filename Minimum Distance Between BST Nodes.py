class Solution(object):
    def minDiffInBST(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()
        return min(vals[i+1] - vals[i]
                   for i in xrange(len(vals) - 1))