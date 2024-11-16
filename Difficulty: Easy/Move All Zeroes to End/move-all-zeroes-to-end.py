#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	p1 = 0
    	p2 = 0
    	while p1 < len(arr):
    	    if arr[p1] == 0:
    	        p2 = max(p2, p1) + 1
    	        while p2 < len(arr) and arr[p2] == 0:
    	            p2 += 1
    	        if p2 == len(arr):
    	            break
    	        arr[p1], arr[p2] = arr[p2], arr[p1]
    	    p1 += 1
    	return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends