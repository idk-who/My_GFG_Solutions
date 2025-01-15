# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        d = {0:-1}
        
        su = 0
        ans = 0
        for ind, ele in enumerate(arr):
            su += ele
            if su - k in d:
                ans = max(ans, ind-d[su-k])
            
            if su not in d:
                d[su] = ind
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends