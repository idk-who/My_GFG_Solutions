#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
        ans = 0
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i > 0:
                        ans += matrix[i-1][j]
                    if j > 0:
                        ans += matrix[i][j-1]
                    if i < n-1:
                        ans += matrix[i+1][j]
                    if j < m-1:
                        ans += matrix[i][j+1]
        return ans
		      


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends