#User function Template for python3
from heapq import heappop, heappush, heapify
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr):
        cost = 0
        h = arr
        heapify(h)
        
        while len(h) > 1:
            p1 = heappop(h)
            p2 = heappop(h)
            
            cost += p1+p2
            
            heappush(h, p1+p2)
        
        return cost
        
        
       
       
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends