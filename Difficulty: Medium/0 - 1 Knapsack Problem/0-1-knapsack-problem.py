#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        def rec(vals, wts, ptr, wt, dp):
            if ptr == len(vals):
                return 0
            
            if (ptr, wt) in dp:
                return dp[(ptr, wt)]
            
            ma = max(
                rec(vals, wts, ptr+1, wt, dp),
                vals[ptr] + rec(vals, wts, ptr+1, wt-wts[ptr], dp) if wts[ptr] <= wt else 0
                )
            
            dp[(ptr, wt)] = ma
            
            return ma
        
        dp = dict()
        
        return rec(val, wt, 0, W, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends