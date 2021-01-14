
class Solution(object):
    def connect(self, root):
        if not root:
            return
        # connect nodes level by level,
        # similar to level order traversal
        queue = collections.deque([root])
        nextLevel = collections.deque([])
        while queue:
            node = queue.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if queue:
                node.next = queue[0]
            if not queue:
                queue, nextLevel = nextLevel, queue
        return root