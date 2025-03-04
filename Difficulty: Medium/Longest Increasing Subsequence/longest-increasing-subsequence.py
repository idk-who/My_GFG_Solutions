class Solution:
    def lis(self, arr):
        # code here
        n = len(arr)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(
                        dp[i],
                        1 + dp[j]
                    )
        
        return max(dp)
        
        
        
            



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends