class Solution:
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        
        if len(arr) < k:
            return -1
        
        def is_poss(pages):
            stud = 1
            su = 0
            for i in arr:
                if i > pages:
                    return False
                su += i
                if su > pages:
                    stud += 1
                    su = i
                    if stud > k:
                        return False
                    
            return True
        
        lo = 0
        hi = sum(arr)
        ans = float('inf')
        
        while lo <= hi:
            m = lo + (hi-lo)//2
            
            if is_poss(m):
                ans = min(ans, m)
                hi = m - 1
            else:
                lo = m + 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends