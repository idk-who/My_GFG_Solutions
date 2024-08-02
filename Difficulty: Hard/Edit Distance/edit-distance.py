class Solution:
    def editDistance(self, s1, s2):
        n1,n2=len(s1),len(s2)
        dp=[[None]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j]=i|j
                else:
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[n1][n2]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends