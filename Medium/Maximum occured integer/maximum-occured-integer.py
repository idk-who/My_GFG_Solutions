#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
        arr = [0]*(maxx+2)
        
        for i in range(n):
            arr[l[i]]+=1
            arr[r[i]+1]-=1
            
        # print(arr)
        carry = 0
        m = -1
        ans = -1
        for i in range(1, maxx+2):
            carry += arr[i]
            if carry > m:
                m = carry
                ans = i
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends