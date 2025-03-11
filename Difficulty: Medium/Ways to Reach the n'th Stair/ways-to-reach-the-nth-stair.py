
class Solution:
    def countWays(self, n):
        prev = 1
        curr = 1
        
        while n-1:
            curr, prev = curr+prev, curr
            n -= 1
        
        return curr


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends