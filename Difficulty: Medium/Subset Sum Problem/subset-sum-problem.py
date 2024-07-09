#User function Template for python3

from collections import defaultdict

class Solution:
    def isSubsetSum (self, N, arr, s):
        dp = defaultdict(bool)
        def rec(N, arr, s, ptr):
            if s == 0:
                return True
            if s < 0 or ptr == N:
                return False
            if (ptr, s) not in dp:
                dp[(ptr, s)] = rec(N, arr, s, ptr+1) or rec(N, arr, s-arr[ptr], ptr+1)
             
            return dp[(ptr, s)]
        
        
        return rec(N, arr, s, 0)
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends