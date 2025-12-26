class Solution:
    def kthMissing(self, arr, k):
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            m = (lo + hi)//2
            
            missing = arr[m] - (m + 1)
            
            if missing < k:
                lo = m + 1
            else:
                hi = m - 1
        
        return lo + k

            

