class TimeMap(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        left = 0
        right = len(A) - 1
        mid = left
        while left <= right:

            mid = (left + right) // 2
            if A[mid][0] == timestamp:
                break
            if A[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        tmppp = bisect.bisect(A, (timestamp, chr(127)))
        print(tmppp)
        i = mid
        print(i)
        print([left, right])
        if A[i][0] == timestamp:
            return A[i][1]
        elif left == 0:
            return ""
        else:
            return A[right][1]

