#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        
        dp = dict()
        def rec(n, k, dp):
            if k == 0:
                return 0
            if n == 1:
                return k
            
            if (n, k) in dp:
                return dp[(n, k)]
            
            mi = float("inf")
            for i in range(1, k+1):
                mi = min(
                    mi,
                    1 + max(
                        rec(n-1, i-1, dp),
                        rec(n, k-i, dp)
                        )
                    )
            dp[(n, k)] = mi        
            
            return mi
        
        return rec(n, k, dp)


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
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends