#User function Template for python3

class Solution:
    def minimizeCost(self, height, n, k):
        dp = [-1]*n
        dp[0] = 0
        
        for i in range(1, n):
            mi = float('inf')
            for j in range(i - min(k, i), i):
                mi = min(mi, abs(height[i]-height[j])+dp[j])
            dp[i] = mi
        
        return dp[-1]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimizeCost(height, n, k))
# } Driver Code Ends