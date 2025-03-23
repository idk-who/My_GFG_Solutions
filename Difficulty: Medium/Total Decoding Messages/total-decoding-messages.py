from functools import cache
class Solution:
	def countWays(self, digits):
	    @cache
		def rec(ptr):
		    if ptr >= len(digits):
		        return 1
		    if digits[ptr] == '0':
		        return 0
		    if 10 <= int(digits[ptr:ptr+2]) <= 26:
		        return rec(ptr+1) + rec(ptr+2)
		    else:
		        return rec(ptr+1)
	    return rec(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends