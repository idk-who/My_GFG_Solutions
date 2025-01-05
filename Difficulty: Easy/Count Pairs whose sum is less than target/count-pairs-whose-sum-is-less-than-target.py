#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        arr.sort()
        
        cnt = 0
        le = 0
        ri = len(arr) - 1
        
        while le < ri:
            if arr[le]+arr[ri] < target:
                cnt += ri - le
                le += 1
            else:
                ri -= 1
        
        return cnt
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends