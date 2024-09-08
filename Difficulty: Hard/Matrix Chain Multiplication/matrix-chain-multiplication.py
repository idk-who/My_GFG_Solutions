#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        dp = dict()
        def rec(arr, i, j, dp):
            if j - i == 1:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            mi = float("inf")
            for k in range(i+1, j):
                mi = min(
                    mi,
                    arr[i]*arr[k]*arr[j] + rec(arr, i, k, dp) + rec(arr, k, j, dp) 
                    )
            dp[(i, j)] = mi
            
            return mi
        
        return rec(arr, 0, len(arr)-1, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends