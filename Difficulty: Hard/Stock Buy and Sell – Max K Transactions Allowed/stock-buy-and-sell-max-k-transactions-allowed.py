class Solution:
    def maxProfit(self, prices, k):
        dp = [
            [-1]*(2*k+1) for j in range(len(prices))
            ]
        def rec(ptr, k):
            if ptr == len(prices):
                return 0
            if k == 0:
                return 0
            
            if dp[ptr][k] != -1:
                return dp[ptr][k]
            
            money = rec(ptr+1, k)
            
            if not k&1:
                temp = -prices[ptr]+rec(ptr+1, k-1)
            else:
                temp = prices[ptr]+rec(ptr+1, k-1)
            
            if temp > money:
                money = temp
            
            dp[ptr][k] = money
            
            return money
        
        return rec(0, 2*k)
        
        
                


#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends