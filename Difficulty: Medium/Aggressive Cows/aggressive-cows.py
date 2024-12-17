#User function Template for python3


class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        
        def is_poss(min_dist):
            cows = 1
            dist = 0
            for i in range(1, n):
                dist += stalls[i] - stalls[i-1]
                if dist >= min_dist:
                    cows += 1
                    dist = 0
            return cows >= k
        
        lo = 0
        hi = (stalls[-1] - stalls[0])//(k-1)
        ans = float("-inf")
        
        while lo <= hi:
            m = (lo+hi)//2
            
            if is_poss(m):
                if m > ans:
                    ans = m
                lo = m + 1
            else:
                hi = m - 1
        
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
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends