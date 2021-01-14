# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA.next == None or headB.next == None:
            return None
        l1 = ListNode(None)
        l2 = ListNode(None)
        while l1 != None and l2 != None:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
            if l1 == None:
                l1 = headA
            if l2 == None:
                l2 = headB
        return None
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
