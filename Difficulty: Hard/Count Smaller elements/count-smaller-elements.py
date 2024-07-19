#User function Template for python3
class Solution:

	def constructLowerArray(self,arr):
		sarr = list(sorted(arr))
		n = len(arr)
		
		def search(arr, n):
		    l = 0 
		    r = len(arr)
		    ind = -1
		    while l <= r:
		        m = l + (r-l)//2
		        
		        if arr[m] == n:
		            ind = m
		            r = m - 1
		        elif arr[m] > n:
		            r = m-1
		        else:
		            l = m+1
		    return ind
		
		ans = [0]*n
		for i in range(n):
		    temp = search(sarr, arr[i])
		  #  print(sarr, temp)
		    ans[i] = temp
		    sarr.pop(temp)
		
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends