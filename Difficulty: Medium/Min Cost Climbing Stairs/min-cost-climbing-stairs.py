#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        one, two = cost[0], cost[1]
        ptr = 2
        
        while ptr < len(cost):
            one, two = two, min(one, two)+cost[ptr]
            ptr += 1
        
        return min(one, two)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends