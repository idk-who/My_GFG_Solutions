
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        
        """
        there are two condition  either we can take a amtching element or not take
        """
        
        # def solve(i, j, s1, s2, dp):
        #     nonlocal mode
        #     if j >= len(s2):
        #         return 1
        #     if i >= len(s1):
        #         return 0
                
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     take = 0
        #     if s1[i] == s2[j]:
        #         take = solve(i+1, j+1, s1, s2, dp)
                
        #     notTake = solve(i+1, j, s1, s2, dp)
            
        #     dp[i][j] = (take+notTake)%mode
        #     return dp[i][j]
        
        # return solve(0, 0, s1, s2, dp) % mode
        mode = 10**9+7
        n1, n2 = len(s1), len(s2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        for i in range(0, n1+1):
            dp[i][n2] = 1
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] += dp[i+1][j+1]%mode
                    
                dp[i][j] += dp[i+1][j] %mode
            
        return dp[0][0]%mode



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends