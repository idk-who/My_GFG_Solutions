#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        arr.sort()
        ptr = 0
        while ptr < len(arr) and arr[ptr] <= 0:
            ptr += 1
        if ptr == len(arr) or arr[ptr] != 1:
            return 1
        ptr += 1
        while ptr < len(arr) and (arr[ptr-1] + 1 == arr[ptr] or arr[ptr-1] == arr[ptr]):
            ptr += 1
        return arr[ptr-1]+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends