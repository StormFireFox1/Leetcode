class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        if len(t) == len(s):
            return 1 if t == s else 0

        dp = [[0 for i in range(len(s))] for j in range(len(t))]

        dp[-1][-1] = 1 if s[-1] == t[-1] else 0

        for i in range(len(t) - 1, -1, -1):
            for j in range(len(s) - 2, -1, -1):
                # '-2' is above because we've done the first one as the base case

                dp[i][j] = dp[i][j + 1]

                # special case for bottom row
                if t[i] == s[j] and i == len(t) - 1:
                    dp[i][j] += 1

                # general case
                elif t[i] == s[j]:
                    dp[i][j] += dp[i + 1][j + 1]

                return dp[0][0]
