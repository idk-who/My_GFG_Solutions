class Solution:
    def count(self, coins, su):
        # code here 
        n = len(coins)
        dp = [[-1]*(su+1) for i in range(n)]
        
        def rec(ptr, su):
            if su == 0:
                return 1
            if ptr == n or su < 0:
                return 0
            
            if dp[ptr][su] != -1:
                return dp[ptr][su]
            
            poss = (
                rec(ptr, su-coins[ptr]) +
                rec(ptr+1, su)
            )
            
            dp[ptr][su] = poss
            
            return poss
        
        return rec(0, su)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends