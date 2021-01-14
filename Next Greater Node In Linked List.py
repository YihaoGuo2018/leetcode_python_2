class Solution(object):
    def nextLargerNodes(self, head):
        res, stack = [], []
        while head:
            print(res)
            print(stack)
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        print(res)
        print(stack)
        return res