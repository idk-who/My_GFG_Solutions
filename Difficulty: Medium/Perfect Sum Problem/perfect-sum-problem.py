#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, s):
		dp = dict()
		
		def helper(arr, ptr, su):
		    if su < 0:
		        return 0
		    if ptr == len(arr):
		        return su == 0
            if (ptr, su) not in dp:
                dp[(ptr, su)] = (helper(arr, ptr+1, su)%(10**9+7) + helper(arr, ptr+1, su-arr[ptr])%(10**9+7))%(10**9+7)
            return dp[(ptr, su)]
        
        return helper(arr, 0, s)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends