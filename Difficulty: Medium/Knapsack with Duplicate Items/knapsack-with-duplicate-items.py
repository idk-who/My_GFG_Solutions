#User function Template for python3
import sys
        
sys.setrecursionlimit(99999)

class Solution:
    def knapSack(self, N, W, val, wt):

        
        dp = [[-1]*(W+1) for _ in range(N)]
        
        def rec(N, vals, wts, ptr, w, dp):
            if ptr == N or w == 0:
                return 0
            
            if dp[ptr][w] == -1:
                dp[ptr][w] = max(
                    rec(N, vals, wts, ptr+1, w, dp),
                    vals[ptr] + rec(N, vals, wts, ptr, w-wts[ptr], dp) if w-wts[ptr] >= 0 else 0
                    )
            return dp[ptr][w]
        
        return rec(N, val, wt, 0, W, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends