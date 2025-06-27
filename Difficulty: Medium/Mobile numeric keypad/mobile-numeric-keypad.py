class Solution:
    dir=[(0,0),(0,1),(0,-1),(1,0),(-1,0)]
    def isValid(self,x,y):
        return (1<=x<=3 and 1<=y<=3) or (x==4 and y==2)
    def getCount(self, n):
        dp=[[[0]*(n+1) for _ in range(4)] for _ in range(5)]
        for k in range(1,n+1):
            for i in range(1,5):
                for j in range(1,4):
                    if self.isValid(i,j):
                        if k==1:
                            dp[i][j][k]=1
                        else:
                            for dx,dy in self.dir:
                                x,y=i+dx,j+dy
                                if self.isValid(x,y):
                                    dp[i][j][k]+=dp[x][y][k-1]
        return sum(dp[i][j][n] for i in range(1,5) for j in range(1,4))