class Solution(object):
    def flatten(self, head):
        childhead, childtail = self.help(head)
        tmp = childhead
        while tmp:
            print("  ")
            if tmp.prev:
                print(tmp.prev.val)
            print(tmp.val)
            tmp = tmp.next
        while tmp:
            tmp = tmp.next
        return childhead

        """
        :type head: Node
        :rtype: Node
        """

    def help(self, node):
        savehead = node
        savetail = None
        while node:
            if node.child:
                childhead, childtail = self.help(node.child)
                tmpnodenext = node.next
                node.next = childhead
                childhead.prev = node
                if tmpnodenext:
                    print(tmpnodenext.val)
                    tmpnodenext.prev = childtail
                if childtail:
                    childtail.next = tmpnodenext
                node.child = None
                savetail = node
                node = node.next
            else:
                savetail = node
                node = node.next

        return savehead, savetail

