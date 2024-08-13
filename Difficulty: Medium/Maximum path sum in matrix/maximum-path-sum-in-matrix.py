#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        dp = dict()
        def rec(mat, i, j, dp):
            if not 0 <= j < N: return 0
            if i == N:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            ma = mat[i][j] + max(
                rec(mat, i+1, j, dp),
                rec(mat, i+1, j-1, dp),
                rec(mat, i+1, j+1, dp)
                )
            
            dp[(i, j)] = ma
            
            return ma
        
        ans = 0
        
        for j in range(N):
            ans = max(
                ans,
                rec(Matrix, 0, j, dp)
                )
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends