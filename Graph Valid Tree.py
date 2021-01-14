class Solution(object):
    dic = {}
    dic2 = {}
    def validTree(self, n, edges):
        for s in range(n):
            self.dic[s] = 0
        if self.sep(edges) == False:
            return False
        for s in range(n):
            self.dic[s] = 0
            self.dic2[s] = []
        for edge in edges:
            self.dic2[edge[0]].append(edge[1])
        return self.circle(0)
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
    def circle(self, n):
        if n == len(self.dic):
            return True
        for num in self.dic2[n]:
            if self.dic[num] = 1:
                return False
            self.dic[num] += 1
            if self.circle(num) == False:
                return False
            self.dic[num] -= 1

        return True

    def sep(self, edges):
        for edge in edges:
            self.dic[edge[0]] += 1
            self.dic[edge[1]] += 1
        for k in self.dic.keys():
            if self.dic[k] == O:
                return False
        return True