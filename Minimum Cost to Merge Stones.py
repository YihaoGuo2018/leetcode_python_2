class Solution:

    def mergeStones(self, s, K):
        N = len(s)
        if (N-1) % (K-1): return -1
        preS= [0] * (N+1)
        for i in range(1,N+1):
            preS[i]=s[i-1]+preS[i-1]
        M = [[float('inf')]*N for _ in range(N)]
        def dp(i, j):
            if M[i][j] == float('inf'):
                if j - i + 1 < K:
                    M[i][j] = 0
                else:
                    M[i][j]=min(dp(i, k) + dp(k+1,j) for k in range(i, j, K - 1))
                    if (j-i)%(K-1)==0:
                        M[i][j]+=preS[j+1]-preS[i]
            return M[i][j]
        return dp(0,N-1)