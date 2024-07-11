from typing import List


class Solution:
    dir=[(1,0),(0,1),(-1,0),(0,-1)]
    
    def dfs(self,grid,i,j,group):
        n=len(grid)
        grid[i][j]=group
        val=0
        for dx,dy in self.dir:
            iNew,jNew=i+dx,j+dy
            if (0<=iNew<n and 0<=jNew<n) and grid[iNew][jNew]==1:
                val+=self.dfs(grid,iNew,jNew,group)
        return val+1
    
    def MaxConnection(self, grid):
        n=len(grid)
        group=2
        map=dict()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    map[group]=self.dfs(grid,i,j,group)
                    group+=1
        val=map.get(2,0)
        if val==n*n:
            return n*n
        elif val==0:
            return 1
        ans=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    s=set()
                    curr=0
                    for dx,dy in self.dir:
                        iNew,jNew=i+dx,j+dy
                        if (0<=iNew<n and 0<=jNew<n) and (grid[iNew][jNew] not in s):
                            curr+=map.get(grid[iNew][jNew],0)
                            s.add(grid[iNew][jNew])
                    ans=max(ans,curr+1)
        return ans


#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends