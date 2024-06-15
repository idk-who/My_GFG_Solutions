#User function Template for python3
class Solution:
	def getCount(self, n):
		self.buttons = [
		    [0, 8],
		    [1, 2, 4], 
		    [2, 1, 3, 5],
		    [3, 2, 6],
		    [4, 1, 5, 7], 
		    [5, 2, 4, 6, 8],
		    [6, 3, 5, 9],
		    [7, 4, 8],
		    [8, 7, 0, 9, 5],
		    [9, 6, 8]
		    ]
		self.dp = [[-1]*10 for _ in range(n+1)]
		ans = 0
        for i in range(10):
            ans += self.helper(n, i)
        
        return ans
		 
		
	def helper(self, n, b):
        if n == 1:
            return 1
        
        if self.dp[n][b] == -1:
            temp = 0
            for i in self.buttons[b]:
                temp += self.helper(n-1, i)
            self.dp[n][b] = temp
        
        return self.dp[n][b]
	   

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends