#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        def rec(n, x, y, z, dp):
            if n == 0:
                return 0
            if n < 0:
                return float("-inf")
            
            if n in dp:
                return dp[n]
            
            ma = max(
                1+rec(n-x, x, y, z, dp),
                1+rec(n-y, x, y, z, dp),
                1+rec(n-z, x, y, z, dp)
                )
            dp[n] = ma
            
            return ma
        
        ans = rec(n, x, y, z, dict())
        
        return 0 if ans == float("-inf") else ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends