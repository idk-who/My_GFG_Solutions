class Solution:
    def findPeakGrid(self, mat):
        """for each column, find the max value
           and put into an array. now it becomes
           a 1D array. the problem become 1D search.
        """
        n = len(mat[0])
        def max_v(i):
            nonlocal mat
            return max((mat[j][i], j) for j in range(len(mat)))

        max_vals = [max_v(i) for i in range(n)]

        def peak(max_vals):
            lo, hi = 0, len(max_vals) - 1
            while lo <= hi:
                mi = lo+(hi-lo)//2 
                if 0 < mi < len(max_vals) - 1:
                    if max_vals[mi-1][0] <= max_vals[mi][0] >= max_vals[mi+1][0]:
                        return max_vals[mi][1], mi
                    if max_vals[mi-1][0] > max_vals[mi][0]:
                        hi = mi - 1 
                    else:
                        lo = mi + 1 
                elif mi == 0:
                    if max_vals[mi][0] >= max_vals[mi+1][0]:  # Changed > to >=
                        return max_vals[mi][1], mi
                    else:
                        lo = mi + 1
                else:
                    if max_vals[mi][0] >= max_vals[mi-1][0]:  # Changed > to >=
                        return max_vals[mi][1], mi
                    else:
                        hi = mi -1 
        
        if len(max_vals) == 1:
            return max_vals[0][1], 0  # Also fixed this to return correct row
            
        return peak(max_vals)