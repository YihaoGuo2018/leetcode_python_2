class Solution:
    def highFive(self, items):
        d = {}
        for i in items:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
        re = []
        for i in d:
            t = d[i]
            t.sort(reverse = True)
            s = sum(t[0:5])
            s = s//5
            re.append([i,s])
        return re