class Solution:
    def lcs(self, s1, s2):
        # code here
        dp = [[-1]*len(s2) for _ in range(len(s1))]
        def rec(p1, p2):
            if p1 == len(s1) or p2 == len(s2):
                return 0
            if dp[p1][p2] != -1:
                return dp[p1][p2]
            
            if s1[p1] == s2[p2]:
                ma = 1 + rec(p1+1, p2+1)
            else:
                ma = max(
                    rec(p1+1, p2),
                    rec(p1, p2+1)
                )
            
            dp[p1][p2] = ma
            
            return ma
        
        return rec(0, 0)

#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the lcs function and print the result
        print(ob.lcs(s1, s2))
        print("~")

# } Driver Code Ends