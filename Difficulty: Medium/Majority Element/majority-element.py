#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        arr.sort()
        n = len(arr)
        if arr[0] != arr[n//2] and arr[-1] != arr[(n-1)//2]:
            return -1
        return arr[n//2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends