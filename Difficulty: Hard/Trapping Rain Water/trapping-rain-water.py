
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        
        suff = [0]*n
        
        ma = 0
        for i in range(n-1, -1, -1):
            suff[i] = ma
            ma = max(ma, arr[i])
        
        ans = 0
        
        ma = 0
        
        for i in range(n):
            ans += max(
                min(ma, suff[i]) - arr[i],
                0)
            ma = max(ma, arr[i])
            
        return ans
        

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends