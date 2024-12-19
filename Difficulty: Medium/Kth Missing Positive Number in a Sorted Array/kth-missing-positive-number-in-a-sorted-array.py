from bisect import bisect_left as bisect

class Solution:
    def kthMissing(self, arr, k):
        if arr[0] > k: return k
        
        lo = 1
        hi = len(arr) - 1
        
        while lo <= hi:
            m = (lo + hi)//2
            
            missing = arr[m] - (m + 1)
            
            if missing < k:
                lo = m + 1
            else:
                hi = m - 1
        
        return hi + k + 1
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends