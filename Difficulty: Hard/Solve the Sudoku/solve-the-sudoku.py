#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        def solve(grid):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        for c in range(1, 10):
                            if is_valid(grid, i, j, c):
                                grid[i][j] = c
                                if solve(grid):
                                    return True
                                grid[i][j] = 0
                        return False
            
            return True
            
        
        def is_valid(grid, i, j, c):
            for r in range(9):
                if grid[r][j] == c or grid[i][r] == c: return False
            
            ni = i//3 * 3
            nj = j//3 * 3
            for ti in range(ni, ni+3):
                for tj in range(nj, nj+3):
                    if grid[ti][tj] == c:
                        return False
            return True
        
        return solve(grid)
                        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        
        for i in arr:
            print(*i, end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends