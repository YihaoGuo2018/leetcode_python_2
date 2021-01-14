# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        savesmall = ListNode(0)
        currsmall = savesmall
        savesbig = ListNode(0)
        currbig = savesbig

        curr = head
        while curr:

            if curr.val < x:
                tmp = curr.next
                curr.next = None
                currsmall.next = curr
                currsmall = currsmall.next
                curr = tmp
            else:
                tmp = curr.next
                curr.next = None
                currbig.next = curr
                currbig = currbig.next
                curr = tmp
        currsmall.next = savesbig.next
        return savesmall.next

        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
