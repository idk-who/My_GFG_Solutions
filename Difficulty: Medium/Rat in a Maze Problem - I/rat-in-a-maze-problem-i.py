from typing import List

class Solution:
    def findPath(self, grid: List[List[int]]) -> List[str]:
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 0 or grid[-1][-1] == 0: return []
        
        ans = []
        
        def rec(grid, i, j, path, ans):
            if i == n-1 and j == m-1:
                ans.append("".join(path))
                return 
            
            if i+1<n and grid[i+1][j]:
                grid[i+1][j] = 0
                path.append('D')
                rec(grid, i+1, j, path, ans)
                path.pop()
                grid[i+1][j] = 1
            
            if i-1>=0 and grid[i-1][j]:
                grid[i-1][j] = 0
                path.append('U')
                rec(grid, i-1, j, path, ans)
                path.pop()
                grid[i-1][j] = 1
            
            if j+1<m and grid[i][j+1]:
                grid[i][j+1] = 0
                path.append('R')
                rec(grid, i, j+1, path, ans)
                path.pop()
                grid[i][j+1] = 1
            
            if j-1>=0 and grid[i][j-1]:
                grid[i][j-1] = 0
                path.append('L')
                rec(grid, i, j-1, path, ans)
                path.pop()
                grid[i][j-1] = 1
        
        ans = []
        grid[0][0] = 0
        rec(grid, 0, 0, [], ans)
        grid[0][0] = 1
        return ans

#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends