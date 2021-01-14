import heapq


class ppp:
    def __init__(self, word, times):
        self.word = word
        self.times = times

    def __lt__(self, other):
        if self.times == other.times:
            return self.word < other.word
        else:
            return self.times < other.times


class Solution(object):
    def topKFrequent(self, words, k):
        save = {}
        for word in words:
            if word in save:
                save[word] += 1
            else:
                save[word] = 1
        print(save)
        heap = []

        for word in save.keys():
            tmp = ppp(str(word), save[word])
            heapq.heappush(heap, tmp)
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort()
        print("i" > "love")
        out = []
        for word in heap:
            out.append(word.word)
        return out
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
