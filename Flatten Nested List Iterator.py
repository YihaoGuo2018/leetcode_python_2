class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.ls = self.flatten(nestedList)
        self.ls = self.ls[::-1]
        print(self.ls)
    def flatten(self, ls):

        res = []
        for item in ls:

            if item.isInteger():
                res.append(item.getInteger())
            else:
                res.extend(self.flatten(item.getList()))
        return res

    def next(self):
        """
        :rtype: int
        """
        return self.ls.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.ls) > 0