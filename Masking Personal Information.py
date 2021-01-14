class Solution(object):
    def maskPII(self, S):
        if '@' in S: #email
            first, after = S.split('@')
            return "{}*****{}@{}".format(
                first[0], first[-1], after).lower()

        else: #phone
            digits = filter(unicode.isdigit, S)
            local = "***-***-{}".format(digits[-4:])
            if len(digits) == 10:
                return local
            return "+{}-".format('*' * (len(digits) - 10)) + local