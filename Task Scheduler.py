class Solution(object):
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        t = dict(collections.Counter(tasks))
        print(t)
        t = list(t.items())
        t.sort(key=lambda p: p[1], reverse=True)
        print(t)
        p = [value for key, value in t]
        # t = sorted（t, key = lambda p :p[1])
        time = 0
        while (p[0] > 0):
            print(p)
            i = 0
            now = 0
            while i <= n and p[0] > 0:
                if now < len(p):
                    p[now] -= 1
                    now += 1

                i += 1
                time += 1
            p.sort(reverse=True)
        return time
        print(time)
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
