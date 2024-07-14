#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # calc string that does not have consecutive 1's
        
        dp = [[0, 0] for _ in range(n+1)]
        dp[1] = [1, 1]
        
        for i in range(2, n+1):
            dp[i] = [(dp[i-1][0]+dp[i-1][1]) % (10**9+7), dp[i-1][0]]
        
        return ((1<<n)-(dp[n][0] + dp[n][1])) % (10**9+7)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends