
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        self.dp = dict()
        
        return self.helper(n, w, cost)
        
        
    def helper(self, n, w, cost):
        if w < 0:
            return float("inf")
        elif w == 0:
            return 0
        
        if w not in self.dp:
            min_cost = float("inf")
            for i in range(n):
                temp = cost[i] + self.helper(n, w-1-i, cost)
                min_cost = min(min_cost, temp)
            self.dp[w] = min_cost
        
        return self.dp[w]
        
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends