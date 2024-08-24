#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        def rec(wts, vals, ptr, wt, dp):
            if ptr == len(wts) or wt == 0:
                return 0
            
            if (ptr, wt) in dp:
                return dp[(ptr, wt)]
            
            ma = max(
                rec(wts, vals, ptr+1, wt, dp),
                vals[ptr]+rec(wts, vals, ptr+1, wt-wts[ptr], dp) if wt-wts[ptr] >= 0 else 0
                )
            
            dp[(ptr, wt)] = ma
            
            return ma
        
        return rec(wt, val, 0, W, dict())

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends