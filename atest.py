class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not len(s):
            return 0
        dict = {}
        left, right = 0, 0
        n = len(s)
        maxL = 1
        while right < n:
            char = s[right]
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
            while left <= right and len(dict) > 2:
                tmp = s[left]
                dict[tmp] -= 1
                if dict[tmp] == 0:
                    dict.pop(tmp)
                left += 1
            maxL = max(right - left + 1, maxL)
            right += 1
        return maxL
