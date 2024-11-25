#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		ma, mi = 1, 1
		ans = arr[0]
		for i in arr:
		    candidiates = (ma*i, i, mi*i)
		    ma = max(candidiates)
		    mi = min(candidiates)
		    ans = max(ans, ma)
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends