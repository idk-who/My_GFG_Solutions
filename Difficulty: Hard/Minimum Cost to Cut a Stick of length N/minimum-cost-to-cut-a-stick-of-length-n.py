class Solution:
    def minCutCost(self, n, cuts):
        from functools import cache
        cuts.extend([0, n])
        cuts.sort()
        
        @cache
        def dfs(start=0, end=len(cuts) - 1):
            if end - start == 1:
                return 0
            return (
                cuts[end] - cuts[start]
                + min(dfs(start, mid) + dfs(mid, end) for mid in range(start + 1, end))
            )
        
        return dfs()