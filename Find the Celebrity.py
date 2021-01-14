class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0

        # if celebrity > candidate, candidate must change to the celebrity, cause (knows(candidate, celebrity) == True)
        # if candidate == celebrity: candidate won't change, cause celebrity knows nobody.
        # after the loop, candidate is the only one can be the celebrity
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # check people < candidate
        for i in range(candidate):
            if knows(candidate, i) or not (knows(i, candidate)):
                return -1

        # check if people > candidate are all knows the candidate
        for i in range(candidate + 1, n):
            if not knows(i, candidate):
                return -1

        return candidate