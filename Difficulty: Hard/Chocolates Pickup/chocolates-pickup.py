class Solution:
    def func(self, ind1, ind2, ind3, n, m , grid):
        if ind1 < 0 or ind1 >= n or ind2 < 0 or ind2 >= m or ind3 < 0 or ind3 >= m:
            return 0
        if self.dp[ind1][ind2][ind3] != -1:
            return self.dp[ind1][ind2][ind3]
        ans = 0
        op1 = grid[ind1][ind2]
        op2 = grid[ind1][ind3]
        new_ind1 = ind1 + 1
        for i in range(3):
            new_ind2 =  ind2 + self.range2[i] 
            for j in range(3):
                new_ind3 = ind3 + self.range2[j]
                if new_ind2 == new_ind3:
                    continue
                op = self.func(new_ind1, new_ind2, new_ind3, n, m, grid)
                ans = max(ans, op)
        self.dp[ind1][ind2][ind3] = ans + op1 + op2
        return self.dp[ind1][ind2][ind3]
        
    def maxChocolate(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        self.dp = [[[-1 for i in range(m+1)] for _ in range(m+1)] for _ in range(n+1)]
        self.range1 = [1, 1, 1]
        self.range2 = [-1, 0, 1]
        self.dp[0][0][m-1] = self.func(0, 0, m - 1, n, m, grid) 
        return self.dp[0][0][m-1]