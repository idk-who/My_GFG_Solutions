#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        
        if n < 3:
            return 1
        
        a, b, c = 1, 1, 1
        
        for i in range(n-2):
            c, b, a = (b+a)%1000000007, c, b
        
        return c
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends