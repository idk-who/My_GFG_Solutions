#User function Template for python3

class Solution:
    def countMin(self, s):
        rs = s[::-1]
        dp = [[-1]*len(s) for _ in range(len(s))]
        
        def rec(s, rs, p1, p2, dp):
            if p1 == len(s) or p2 == len(rs):
                return 0
            
            if dp[p1][p2] == -1:
                if s[p1] == rs[p2]:
                    dp[p1][p2] = 1 + rec(s, rs, p1+1, p2+1, dp)
                else:
                    dp[p1][p2] = max(
                        rec(s, rs, p1+1, p2, dp),
                        rec(s, rs, p1, p2+1, dp)
                        )
            return dp[p1][p2]
            
        lcs = rec(s, rs, 0, 0, dp)
        return len(s) - lcs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends