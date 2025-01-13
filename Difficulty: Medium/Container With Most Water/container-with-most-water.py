
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        
        le = 0
        ri = n-1
        
        ans = 0
        
        while le < ri:
            ans = max(
                ans,
                min(arr[le], arr[ri])*(ri-le)
            )
            
            if arr[le] < arr[ri]:
                le += 1
            else:
                ri -= 1
        
        return ans
        


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