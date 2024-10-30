#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	d = {}
        ans = 0    	
        arr.sort()
    	for i in arr:
    	    if i-k in d:
    	        ans += d[i-k]
    	    if i in d:
    	        d[i] += 1
    	    else:
    	        d[i] = 1
        
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends