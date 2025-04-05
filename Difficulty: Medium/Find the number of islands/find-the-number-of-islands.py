#User function Template for python3

class Solution:
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        cnt = 0
        def rec(i, j):
            if 0 <= i < n and 0 <= j < m:
                if grid[i][j] == 'L':
                    grid[i][j] = 'W'
                    rec(i+1, j)
                    rec(i-1, j)
                    rec(i, j+1)
                    rec(i, j-1)
                    rec(i-1, j-1)
                    rec(i-1, j+1)
                    rec(i+1, j-1)
                    rec(i+1, j+1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':
                    cnt += 1
                    rec(i, j)
        
        return cnt
        
#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends