# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        savehead = ListNode(0)
        savehead.next = head
        precur = savehead
        while precur.next:

            curr = precur.next
            val = curr.val
            if curr.next and curr.next.val == val:
                while curr.next and curr.next.val == val:
                    curr = curr.next
                print(curr.val)
                precur.next = curr.next
            else:
                precur = precur.next
        return savehead.next

        """
        :type head: ListNode
        :rtype: ListNode
        """
