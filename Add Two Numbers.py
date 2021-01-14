
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = "", ""
        now = l1
        while now != None:
            s1 += str(now.val)
            now = now.next
        now = l2
        while now != None:
            s2 += str(now.val)
            now = now.next
        s1 = s1[::-1]
        s2 = s2[::-1]

        s1 = int(s1)
        s2 = int(s2)
        s3 = s1 + s2

        s3 = str(s3)
        s3 = s3[::-1]
        list1 = ListNode(-1)
        help = list1
        for s in s3:
            t1 = ListNode(int(s))
            help.next = t1
            help = t1
        return list1.next
