class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)

        dp = [[0] * n for _ in range(n)]
        split = [[0] * n for _ in range(n)]
        
        for L in range(2, n):
            for i in range(1, n - L + 1):
                j = i + L - 1
                dp[i][j] = float('inf')
                
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k

        def build(i, j):
            if i == j:
                return chr(ord('A') + i - 1)
            k = split[i][j]
            return "(" + build(i, k) + build(k + 1, j) + ")"
        
        return build(1, n - 1)