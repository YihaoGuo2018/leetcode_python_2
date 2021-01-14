
import itertools
S = "heeellooo"

for k, grp in itertools.groupby(S):
    print(k)
    print(list(grp))