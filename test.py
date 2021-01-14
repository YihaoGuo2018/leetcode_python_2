

# s = "ab"
# s = "aa"
# s = "abc"
# s = "abcb"
s = "abbea"
#
# s = "abbea"

dp = [[[1, s[i]] for i in range(len(s))] for i in range(len(s)) ]

for i in range(len(s)):
    dp[i][i] = [1, s[i]]

for i in range(len(s)):
    for j in range(0, i):

        if s[i] == s[j]:
            if j + 1 == i:
                dp[j][i] = [2, s[i] + s[i]]
print(dp)

for i in range(len(s)):
    for j in range(0, i):
        if s[i] == s[j]:
            if i-1 >= j+1:
                dp[j][i] = [dp[j+1][i-1][0] + 2, s[i] + dp[j+1][i-1][1] + s[i]]
        else:
            if dp[j + 1][i][0] > dp[j][i - 1][0]:
                dp[j][i] = [dp[j + 1][i ][0], dp[j + 1][i][1]]
            else:
                dp[j][i] = [dp[j][i - 1][0], dp[j][i - 1][1]]



lens = 0
out = ""
print(dp)
for i in range(len(s)):
    for j in range(len(s)):
        if dp[j][i][0] >= lens:
            out = dp[j][i][1]
            lens = dp[j][i][0]

print(len(s) - lens)
print(out)

