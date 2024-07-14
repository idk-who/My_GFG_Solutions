
from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        if (sum(arr)+d) & 1: return 0
        target = (sum(arr)+d)//2
        dp = [0]*(target+1)
        
        dp[0] = 1
        if arr[0]<=target:
            dp[arr[0]] += 1
        
        for i in range(1, n):
            for t in range(target, -1, -1):
                if arr[i] <= t:
                    dp[t] = (dp[t] + dp[t-arr[i]]) % (10**9+7)
        return dp[-1]
        
        # if (sum(arr)+d) & 1: return 0
        # target = (sum(arr)+d)//2
        # dp = [[-1]*(target+1) for _ in range(n)]
        # def helper(arr, ptr, t, dp):
        #     if ptr == len(arr):
        #         return t == 0
        #     if t < 0:
        #         return 0
            
        #     if dp[ptr][t] == -1:
        #         dp[ptr][t] = (
        #             helper(arr, ptr+1, t, dp)+ 
        #             helper(arr, ptr+1, t-arr[ptr], dp)
        #             ) % (10**9+7)
        #     return dp[ptr][t] 
        
        # return helper(arr, 0, target, dp)
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends