#User function Template for python3

class Solution:
    def findNth(self,n):
        ans = 0
        base = 1
        
        while n:
            ans += (n%9)*base
            base *= 10
            n //= 9
        
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends