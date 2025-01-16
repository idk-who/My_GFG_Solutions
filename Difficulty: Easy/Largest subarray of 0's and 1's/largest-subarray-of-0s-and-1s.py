class Solution:
    def maxLen(self, arr):
        d = {0:-1}
        
        su = 0
        ans = 0
        for ind, ele in enumerate(arr):
            su += 1 if ele else -1
            
            if su in d:
                ans = max(ans, ind-d[su])
            else:
                d[su] = ind
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends