"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            head = Node(insertVal)
            return head
        precurr = Node(0)
        precurr.next = head
        minv = head.val
        maxv = head.val
        tmp = head.next
        while tmp != head:
            minv = min(minv, tmp.val)
            maxv = max(maxv, tmp.val)
            tmp = tmp.next
        print(maxv)
        print(minv)
        if insertVal > maxv or insertVal <= minv:
            tmp = head
            tmp3 = head
            while not (tmp.val == maxv and tmp.next == minv):
                tmp = tmp.next
            tmp2 = tmp.next
            tmp.next = Node(insertVal)
            tmp.next.next = tmp2
            return precurr.next
        else:
            tmp = head
            while not (tmp.val < insertVal and insertVal <= tmp.next.val):
                tmp = tmp.next
            tmp2 = tmp.next
            print(tmp2.val)
            tmp.next = Node(insertVal)
            tmp.next.next = tmp2

            return precurr.next

        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
