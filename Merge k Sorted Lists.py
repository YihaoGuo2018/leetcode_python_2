# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        l = lists

        out1 = ListNode(None)
        out = ListNode(None)
        while len(l):
            for a in l:
                if a == None:
                    l.remove(a)

            si = 0
            small = l[0].val
            for i in range(len(l)):
                if l[i].val < small:
                    small = l[i].val
                    si = i
            out.val = l[si].val
            l[si] = l[si].next
            for a in l:
                if a == None:
                    l.remove(a)
        return out1



        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
