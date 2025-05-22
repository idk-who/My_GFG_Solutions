class Solution:
    def minDeletions(self,S):
        # code here 
        n = len(S)
    
        # Create a 2D array to store the minimum deletions required for subproblems
        dp = [[0] * n for _ in range(n)]
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    
        # The minimum number of deletions to make a palindrome is stored in dp[0][n-1]
        return dp[0][n-1]