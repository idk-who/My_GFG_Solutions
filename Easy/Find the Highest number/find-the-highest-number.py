#User function Template for python3
from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        lo = 0
        hi = len(a) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if a[mid + 1] > a[mid]:
                lo = mid + 1
            else:
                hi = mid

        return a[lo]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends