#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		
		n, m = len(arr), len(arr[0])
		
		m1 = 0
		i = n-1
		j = m-1
		
		while i >= 0:
		    while j >= 0 and arr[i][j] == 1:
		        j -= 1
		    i -= 1
		if j == m-1: return -1
		for i in range(n):
		    if arr[i][j+1]==1:
		        return i
		
		return 0
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends