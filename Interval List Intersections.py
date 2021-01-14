class Solution(object):
    def intervalIntersection(self, a , b):
            i,j, res = 0, 0, []
            while i < len(a) and j < len(b):
                if a[i][1] < b[j][0]:
                    i += 1
                elif b[j][1] < a[i][0]:
                    j += 1
                else:
                    res.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])]  )
                    if a[i][1] > b[j][1]:
                        j += 1
                    else:
                        i += 1
            return res