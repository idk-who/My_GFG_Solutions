#User function Template for python3

from collections import defaultdict

class Solution:
    def isSubsetSum(self, N, arr, s):
        dp = 1
        
        for n in arr:
            dp |= (dp << n)
        
        return (dp & (1 << s)) != 0
        
    def spOp_isSubsetSum(self, N, arr, s):
        dp = [False]*(s+1)
        dp[0] = True
        if arr[0] <= s:
            dp[arr[0]] = True
        
        new_dp = [False]*(s+1)
        new_dp[0] = True
        
        for i in range(1, N):
            for t in range(1, s+1):
                notTaken = dp[t]
                taken = dp[t-arr[i]] if arr[i]<=t else False
                new_dp[t] = notTaken or taken
            dp[:] = new_dp
        
        return dp[-1]
        
    
    def tab_isSubsetSum(self, N, arr, s):
        dp = [[False]*(s+1) for _ in range(N)]
        
        dp[0][0] = True
        if arr[0] <= s:
            dp[0][arr[0]] = True
            
        for i in range(1, N):
            dp[i][0] = True
            for t in range(1, s+1):
                notTaken = dp[i-1][t]
                
                taken = dp[i-1][t-arr[i]] if arr[i] <= t else False
                
                dp[i][t] = taken or notTaken
        
        return dp[-1][-1]
            
        
    def mem_isSubsetSum(self, N, arr, s):
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