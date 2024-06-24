#User function Template for python3

class Solution:
    def maximumPoints(self, points, n):
        dp = [[-1]*3 for _ in range(n)]
        
        dp[0] = points[0]
        
        for i in range(1,n):
            dp[i] = (
                points[i][0] + max(dp[i-1][1], dp[i-1][2]),
                points[i][1] + max(dp[i-1][0], dp[i-1][2]),
                points[i][2] + max(dp[i-1][1], dp[i-1][0])
                )
        
        return max(dp[-1])
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(points, n))
# } Driver Code Ends