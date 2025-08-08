class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (
                        dp[i-1][j] if p[j-2] == '.' or p[j-2] == s[i-1] else False
                    )

        return dp[len(s)][len(p)]
