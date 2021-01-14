import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        def comp(elem):
            return elem[0]
        intervals.sort(key=comp, reverse = True)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)

