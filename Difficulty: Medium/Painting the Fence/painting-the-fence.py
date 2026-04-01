class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return k * k
            
        same = k
        diff = k * (k - 1)
        
        for i in range(3, n + 1):
            prev_same = same
            same = diff
            diff = (prev_same + diff) * (k - 1)
            
        return same + diff